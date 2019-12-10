# will be putting loading code here
from influxdb import InfluxDBClient
import numpy as np
import random
from datetime import datetime
from sklearn.model_selection import train_test_split

db_name = 'sensor_db'

# class labels
# Null=0, Still=1, Walking=2, Run=3, Bike=4, Car=5, Bus=6, Train=7, Subway=8 
def time_diff(time1, time2):
    try:
        m1 = datetime.strptime(time1, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000
    except:
        m1 = datetime.strptime(time1, '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000
    try:
        m2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp() * 1000
    except:
        m2 = datetime.strptime(time2, '%Y-%m-%dT%H:%M:%SZ').timestamp() * 1000

    if abs(m1 - m2) > 10:
        return False
    return True

# # stackoverflow :https://stackoverflow.com/questions/4601373/better-way-to-shuffle-two-numpy-arrays-in-unison
# def unison_shuffled_copies(a, b):
#     assert len(a) == len(b)
#     p = np.random.permutation(len(a))
#     return a[p], b[p]

def query_batch(client_db, start_time, end_time, user):
    series = []
    query_str = 'SELECT "acceleration x", "acceleration y", "acceleration z", '
    query_str += '"gyroscope x", "gyroscope y", "gyroscope z", '
    query_str += '"linear acceleration x", "linear acceleration y", "linear acceleration z" '
    query_str += 'FROM Motion WHERE time >= \'%s\' and time <= \'%s\' and "user" = \'%d\' '%(start_time, end_time, user)
    query_str += 'and "body part" = \'Hips\''
    results_motion = client_db.query(query_str)
    points = results_motion.get_points()
    for point in points:
         series.append(np.asarray(list(point.values())[1:]))

    return np.asarray(series)

def get_motion_data(client_db, points, data_storage, data_labels, label, start_index, user, max_points=562):

    batch = []
    point_index = start_index
    end_index = point_index + max_points
    prev_time = points[0]['time']

    for point in points:
        if time_diff(prev_time, point['time']):
            batch.append(point['time'])
            if len(batch) == 128:
                data_storage[point_index] = query_batch(client_db, batch[0], batch[-1], user)
                data_labels[point_index] = label - 1 # zero based indexing
                point_index += 1
                batch.clear()
        else:
            batch.clear()

        prev_time = point['time']

        if point_index == end_index:
            break
    return point_index


def load_data(client_db):
    
    data_u1_features = np.zeros((4496, 128, 9))
    data_u1_labels = np.zeros((4496, 1))
    u1_point_index = 0
    data_u2_features = np.zeros((4496, 128, 9))
    data_u2_labels = np.zeros((4496, 1))
    u2_point_index = 0
    data_u3_features = np.zeros((4496, 128, 9))
    data_u3_labels = np.zeros((4496, 1))
    u3_point_index = 0
    
    for class_ in [1, 2, 3, 4, 5, 6, 7, 8]:
        query_str = 'SELECT coarse '
        query_str += 'FROM Label WHERE coarse = %d '%(class_)
        query_str += 'GROUP BY "user"'
        results = client_db.query(query_str)

        points_u1 = list(results.get_points(tags={'user': '1'}))
        points_u2 = list(results.get_points(tags={'user': '2'}))
        points_u3 = list(results.get_points(tags={'user': '3'}))
        del results
        
        # want 10,000 data points for all classes train + 3500 test data points
        # from each class we need 1688 points at least
        # from each user per class we need 562 points
        print('Collecting class', class_, 'data...')
        print('U1 data...')
        u1_point_index = get_motion_data(client_db, points_u1, data_u1_features, data_u1_labels, class_, u1_point_index, 1)
        print('U2 data...')
        u2_point_index = get_motion_data(client_db, points_u2, data_u2_features, data_u2_labels, class_, u2_point_index, 2)
        print('U3 data...')
        u3_point_index = get_motion_data(client_db, points_u3, data_u3_features, data_u3_labels, class_, u3_point_index, 3)
        # series = []
        # point_index = 0
        # prev_time = points_u1[0]['time']
        # for point in points_u1:
        #     if time_diff(prev_time, point['time']):
        #         query_str = 'SELECT "acceleration x", "acceleration y", "acceleration z", '
        #         query_str += '"gyroscope x", "gyroscope y", "gyroscope z", '
        #         query_str += '"linear acceleration x", "linear acceleration y", "linear acceleration z" '
        #         query_str += 'FROM Motion WHERE time = \'%s\' and "user" = \'1\' '%(point['time'])
        #         query_str += 'and "body part" = \'Hips\''
        #         results_motion = client_db.query(query_str)
        #         m_point = list(list(results_motion.get_points())[0].values())[1:]
        #         series.append(np.asarray(m_point))
                
        #         if len(series) == 128:
        #             data_u1[point_index] = np.asarray(series)
        #             series.clear()
        #             point_index += 1
        #     else:
        #         series.clear() # try finding continuos series

        #     prev_time = point['time']
    X = np.concatenate((data_u1_features, data_u2_features, data_u3_features))
    y = np.concatenate((data_u1_labels, data_u2_labels, data_u3_labels))
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
        
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database(db_name)

    data = load_data(client)