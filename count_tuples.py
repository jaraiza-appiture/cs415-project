import os
USER_1 = '../data/text_files/'
USER_2 = '../data_2/text_files/'
USER_3 = '../data_3/text_files/'

total_tuples = 0
for user in [USER_1, USER_2, USER_3]:
    for filename in os.listdir(user):
        if filename.endswith(".txt"):
            total_tuples += sum(1 for line in open(user+filename))
        
print('Total Tuples:', total_tuples)