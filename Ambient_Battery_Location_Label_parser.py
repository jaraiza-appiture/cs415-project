from constants import USERS, AMBIENT_BODY_PARTS, BATTERY_BODY_PARTS

def ambientParser(client):
    json_body = []

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
            json_body.clear()


def batteryParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in BATTERY_BODY_PARTS:
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    time,ign1,ign2,blevel,temp = line.split(' ')

                    json_body.append({"measurement":"battery",
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

def locationParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in LOCATION_BODY_PARTS:
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    time,ign1,ign2,accuracy,latitude,longitude,altitude = line.split(' ')

                    json_body.append({"measurement":"location",
                                    "tags":{
                                        "user":user_id,
                                        "body part": body_part
                                    },
                                    "time":time,
                                    "fields":{
                                        "accuracy":accuracy,
                                        "latitude":latitude,
                                        "longitude":longitude,
                                        "altitude":altitude
                                    }
                    })

            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()  # don't forget to clear list for next file
#
# def cellsParser():
#     json_body = []
#
#     with open("Bag_Cells.txt", 'r') as in_file:
#         for line in in_file:
#             features = line.split(' ')
#             time = features[0]
#             ign1 = features[1]
#             ign2 = features[2]
#             num_entries = features[3]
#             for i in range(int(num_entries)):
#                 celltype = features[i+4]
#                 if (celltype == 'LTE'):
#                     for i in range(8):
#                         signallevel = features[i+5]
#                         signalstrength = features[i+6]
#
#                         pass
#                 elif (celltype == 'GSM'):
#                     for i in range(8):
#                         pass
#                 elif (celltype == 'WCDMA'):
#                     for i in range(9):
#                         pass
#
#             break
#
# cellsParser()
# #LTE: 8
# #GSM:7
# #WCDMA:9

def labelParser(client):
    json_body = []
    for user_file, user_id in USERS:
        with open(user_file + "Label.txt", 'r') as in_file:
            for line in in_file:
                features = line.split(' ')
                time = features[0]
                coarse = features[1]
                fine = features[2]
                road = features[3]
                traffic = features[4]
                tunnel = features[5]
                social = features[6]
                food = features[7]

                json_body.append({"measurement":"label",
                                "tags":{
                                    "user":user_id
                                },
                                "time":time,
                                "fields":{
                                    "coarse":coarse,
                                    "fine":fine,
                                    "road":road,
                                    "traffic": traffic,
                                    "tunnel": tunnel,
                                    "social": social,
                                    "food":food
                                }
                })

        if not client.write_points(json_body):
            print('Failed to write to database!')
        json_body.clear()  # don't forget to clear list for next file

