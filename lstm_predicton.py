# Reference: https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition
# Code based on repo above, modified to work with our data
# Modified by: Jovan Araiza

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import metrics
from prep_data import load_data
import os
from influxdb import InfluxDBClient

# Useful Constants

# Those are separate normalized input features for the neural network
INPUT_SIGNAL_TYPES = [
    "hips_acc_x_",
    "hips_acc_y_",
    "hips_acc_z_",
    "hips_gyro_x_",
    "hips_gyro_y_",
    "hips_gyro_z_",
    "hips_linear_acc_x_",
    "hips_linear_acc_y_",
    "hips_linear_acc_z_"
]

# Output classes to learn how to classify
LABELS = [
    "STILL",
    "WALKING",
    "RUNING",
    "BIKE",
    "CAR",
    "BUS",
    "TRAIN",
    "SUBWAY"
]

# LSTM Neural Network's internal structure
N_HIDDEN = 32 # Hidden layer num of features
N_CLASSES = 8 # Total classes (should go up, or should go down)

DB_NAME = 'sensor_db'

def LSTM_RNN(_X, _weights, _biases, n_input, n_steps):
    # Function returns a tensorflow LSTM (RNN) artificial neural network from given parameters.
    # Moreover, two LSTM cells are stacked which adds deepness to the neural network.
    # Note, some code of this notebook is inspired from an slightly different
    # RNN architecture used on another dataset, some of the credits goes to
    # "aymericdamien" under the MIT license.

    # (NOTE: This step could be greatly optimized by shaping the dataset once
    # input shape: (batch_size, n_steps, n_input)
    _X = tf.transpose(_X, [1, 0, 2])  # permute n_steps and batch_size
    # Reshape to prepare input to hidden activation
    _X = tf.reshape(_X, [-1, n_input])
    # new shape: (n_steps*batch_size, n_input)

    # ReLU activation, thanks to Yu Zhao for adding this improvement here:
    _X = tf.nn.relu(tf.matmul(_X, _weights['hidden']) + _biases['hidden'])
    # Split data because rnn cell needs a list of inputs for the RNN inner loop
    _X = tf.split(_X, n_steps, 0)
    # new shape: n_steps * (batch_size, n_hidden)

    # Define two stacked LSTM cells (two recurrent layers deep) with tensorflow
    lstm_cell_1 = tf.contrib.rnn.BasicLSTMCell(N_HIDDEN, forget_bias=1.0, state_is_tuple=True)
    lstm_cell_2 = tf.contrib.rnn.BasicLSTMCell(N_HIDDEN, forget_bias=1.0, state_is_tuple=True)
    lstm_cells = tf.contrib.rnn.MultiRNNCell([lstm_cell_1, lstm_cell_2], state_is_tuple=True)
    # Get LSTM cell output
    outputs, states = tf.contrib.rnn.static_rnn(lstm_cells, _X, dtype=tf.float32)

    # Get last time step's output feature for a "many-to-one" style classifier,
    # as in the image describing RNNs at the top of this page
    lstm_last_output = outputs[-1]

    # Linear activation
    return tf.matmul(lstm_last_output, _weights['out']) + _biases['out']


def extract_batch_size(_train, step, batch_size):
    # Function to fetch a "batch_size" amount of data from "(X|y)_train" data.

    shape = list(_train.shape)
    shape[0] = batch_size
    batch_s = np.empty(shape)

    for i in range(batch_size):
        # Loop index
        index = ((step-1)*batch_size + i) % len(_train)
        batch_s[i] = _train[index]

    return batch_s


def one_hot(y_, n_classes=N_CLASSES):
    # Function to encode neural one-hot output labels from number indexes
    # e.g.:
    # one_hot(y_=[[5], [0], [3]], n_classes=6):
    #     return [[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]]

    y_ = y_.reshape(len(y_))
    return np.eye(n_classes)[np.array(y_, dtype=np.int32)]  # Returns FLOATS

def run_training_testing(X_train, X_test, y_train, y_test):
    
    training_data_count = len(X_train)  # 7352 training series (with 50% overlap between each serie)
    test_data_count = len(X_test)  # 2947 testing series
    n_steps = len(X_train[0])  # 128 timesteps per series
    n_input = len(X_train[0][0])  # 9 input parameters per timestep
    
    # Training
    learning_rate = 0.0025
    lambda_loss_amount = 0.0015
    training_iters = training_data_count * 300  # Loop 300 times on the dataset
    batch_size = 1500
    display_iter = 30000  # To show test set accuracy during training


    # Some debugging info
    print("Some useful info to get an insight on dataset's shape and normalisation:")
    print("(X shape, y shape, every X's mean, every X's standard deviation)")
    print(X_test.shape, y_test.shape, np.mean(X_test), np.std(X_test))
    print("The dataset is therefore properly normalized, as expected, but not yet one-hot encoded.")


    # Graph input/output
    x = tf.placeholder(tf.float32, [None, n_steps, n_input])
    y = tf.placeholder(tf.float32, [None, N_CLASSES])

    # Graph weights
    weights = {
        'hidden': tf.Variable(tf.random_normal([n_input, N_HIDDEN])), # Hidden layer weights
        'out': tf.Variable(tf.random_normal([N_HIDDEN, N_CLASSES], mean=1.0))
    }
    biases = {
        'hidden': tf.Variable(tf.random_normal([N_HIDDEN])),
        'out': tf.Variable(tf.random_normal([N_CLASSES]))
    }

    pred = LSTM_RNN(x, weights, biases, n_input, n_steps)

    # Loss, optimizer and evaluation
    l2 = lambda_loss_amount * sum(
        tf.nn.l2_loss(tf_var) for tf_var in tf.trainable_variables()
    ) # L2 loss prevents this overkill neural network to overfit the data
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred)) + l2 # Softmax loss
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost) # Adam Optimizer

    correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    # To keep track of training's performance
    test_losses = []
    test_accuracies = []
    train_losses = []
    train_accuracies = []

    # Launch the graph
    sess = tf.InteractiveSession(config=tf.ConfigProto(log_device_placement=True))
    init = tf.global_variables_initializer()
    sess.run(init)

    # Perform Training steps with "batch_size" amount of example data at each loop
    step = 1
    while step * batch_size <= training_iters:
        batch_xs =         extract_batch_size(X_train, step, batch_size)
        batch_ys = one_hot(extract_batch_size(y_train, step, batch_size))

        # Fit training using batch data
        _, loss, acc = sess.run(
            [optimizer, cost, accuracy],
            feed_dict={
                x: batch_xs,
                y: batch_ys
            }
        )
        train_losses.append(loss)
        train_accuracies.append(acc)

        # Evaluate network only at some steps for faster training:
        if (step*batch_size % display_iter == 0) or (step == 1) or (step * batch_size > training_iters):

            # To not spam console, show training accuracy/loss in this "if"
            print("Training iter #" + str(step*batch_size) + \
                ":   Batch Loss = " + "{:.6f}".format(loss) + \
                ", Accuracy = {}".format(acc))

            # Evaluation on the test set (no learning made here - just evaluation for diagnosis)
            loss, acc = sess.run(
                [cost, accuracy],
                feed_dict={
                    x: X_test,
                    y: one_hot(y_test)
                }
            )
            test_losses.append(loss)
            test_accuracies.append(acc)
            print("PERFORMANCE ON TEST SET: " + \
                "Batch Loss = {}".format(loss) + \
                ", Accuracy = {}".format(acc))

        step += 1

    print("Optimization Finished!")

    # Accuracy for test data

    one_hot_predictions, accuracy, final_loss = sess.run(
        [pred, accuracy, cost],
        feed_dict={
            x: X_test,
            y: one_hot(y_test)
        }
    )

    test_losses.append(final_loss)
    test_accuracies.append(accuracy)

    print("FINAL RESULT: " + \
        "Batch Loss = {}".format(final_loss) + \
        ", Accuracy = {}".format(accuracy))

    font = {
        'family' : 'Bitstream Vera Sans',
        'weight' : 'bold',
        'size'   : 18
    }
    matplotlib.rc('font', **font)

    width = 12
    height = 12
    plt.figure(figsize=(width, height))

    indep_train_axis = np.array(range(batch_size, (len(train_losses)+1)*batch_size, batch_size))
    plt.plot(indep_train_axis, np.array(train_losses),     "b--", label="train losses")
    plt.plot(indep_train_axis, np.array(train_accuracies), "g--", label="train accuracies")

    indep_test_axis = np.append(
        np.array(range(batch_size, len(test_losses)*display_iter, display_iter)[:-1]),
        [training_iters]
    )
    plt.plot(indep_test_axis, np.array(test_losses),     "b-", label="test losses")
    plt.plot(indep_test_axis, np.array(test_accuracies), "g-", label="test accuracies")

    plt.title("Loss & Accuracy vs Epochs")
    plt.legend(loc='upper right', shadow=True)
    plt.ylabel('Loss & Accuracy)')
    plt.xlabel('Training iteration')
    plt.savefig('./training_results.png')
    plt.show()

    # Results

    predictions = one_hot_predictions.argmax(1)

    print("Testing Accuracy: {}%".format(100*accuracy))

    print("")
    print("Precision: {}%".format(100*metrics.precision_score(y_test, predictions, average="weighted")))
    print("Recall: {}%".format(100*metrics.recall_score(y_test, predictions, average="weighted")))
    print("f1_score: {}%".format(100*metrics.f1_score(y_test, predictions, average="weighted")))

    print("")
    print("Confusion Matrix:")
    confusion_matrix = metrics.confusion_matrix(y_test, predictions)
    print(confusion_matrix)
    normalized_confusion_matrix = np.array(confusion_matrix, dtype=np.float32)/np.sum(confusion_matrix)*100

    print("")
    print("Confusion matrix (normalized to % of total test data):")
    print(normalized_confusion_matrix)
    print("Note: training and testing data is not equally distributed amongst classes, ")
    print("so it is normal that more than a 6th of the data is correctly classifier in the last category.")

    # Plot Results:
    width = 12
    height = 12
    plt.figure(figsize=(width, height))
    plt.imshow(
        normalized_confusion_matrix,
        interpolation='nearest',
        cmap=plt.cm.rainbow
    )
    plt.title("Confusion matrix \n(normalized to % of total test data)")
    plt.colorbar()
    tick_marks = np.arange(N_CLASSES)
    plt.xticks(tick_marks, LABELS, rotation=90)
    plt.yticks(tick_marks, LABELS)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig("./Confusion_mat.png")
    plt.show()

if __name__ == '__main__':
    # Input Data
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database(DB_NAME)
    print('Loading data...')
    X_train, X_test, y_train, y_test = load_data(client)
    run_training_testing(X_train, X_test, y_train, y_test)
    