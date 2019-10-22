from constants import USERS, AMBIENT_BODY_PARTS, BATTERY_BODY_PARTS

#not done

# #dont actually think we need infParser so didnt finish it. Might need to finish if we need it but I dont think we do
# def infParser():
#     json_body = []
#     # f = open(USER_1 + '00inf.txt', 'r')
#
#     f = open('00inf.txt','r')
#     lines = f.readlines()
#     userid = lines[0].split(' ')[1]
#     timesmin = lines[1].split(' ')[1]
#     timesmax = lines[2].split(' ')[1]
#     starttime = lines[3].split(' ')[1]
#     startdate = lines[3].split(' ')[2]
#     millength = lines[4].split(' ')[1]
#     recordId = lines[5].split(' ')[1]

def ambientParser(client):
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')


    for user_file, user_id in USERS:
        for body_part_file in AMBIENT_BODY_PARTS:
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    time, ign1, ign2, lumix, temp, ign3 = line.split(' ')

                    json_body.append({"measurement":"Ambient",
                            "tags":{
                                "user":user_id,
                                "body part": body_part
                            },
                            "time": time,
                            "fields":{
                                "lumix":lumix,
                                "temperature":temp}
                            })
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear() # don't forget to clear list for next file


def batteryParser(client):
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')
    # f=open('Bag_Battery.txt','r')

    for user_file, user_id in USERS:
        for body_part_file in BATTERY_BODY_PARTS:
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    time,ign1,ign2,blevel,temp = line.split(' ')

                    json_body.append({"measurement":"Battery",
                                "tags":{
                                    "user":user_id,
                                    "body part": body_part
                                },
                                "time":time,
                                "fields":{
                                    "battery level":blevel,
                                    "temperature":temp}
                    })
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()

#tried labelstrack main
# but not exactly sure how we store start/end run time in db. I just chose start with end as field
# def labelstrackmain():
#     json_body = []
#     # f = open(USER_1 + '00inf.txt', 'r')
#     f=open('labels_track_main.txt','r')
#
#     for line in f:
#         starttime,endtime,activity = line.split(' ')
#
#     data = {"measurement":"labelstrackmain",
#             "tags":{"user":1},
#             "time":starttime,
#             "fields":{"end time":endtime,
#                       "activity":activity}
#             }
