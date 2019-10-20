from constants import USERS, MOTION_BODY_PARTS, API_BODY_PARTS, GPS_BODY_PARTS

def MotionParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in MOTION_BODY_PARTS:
            # get body part to add as tag for all data points in this file
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    # some of the features may be NaN values
                    features = line.split(' ')
                    # time in ms
                    ti = features[0]
                    acX = features[1]
                    acY = features[2]
                    acZ = features[3]
                    gyX = features[4]
                    gyY = features[5]
                    gyZ = features[6]
                    mgX = features[7]
                    mgY = features[8]
                    mgZ = features[9]
                    oriW = features[10]
                    oriX = features[11]
                    oriY = features[12]
                    oriZ = features[13]
                    gX = features[14]
                    gY = features[15]
                    gZ = features[16]
                    linX = features[17]
                    linY = features[18]
                    linZ = features[19]
                    pre = features[20]
                    alt = features[21]
                    temp = features[22]

                json_body.append({
                    "measurement": "Motion",
                    "tags": {
                        "user": user_id,
                        "body part": body_part # need to get specific body part data later
                    },
                    "time": ti,
                    "fields": {
                        "acceleration x": acX,
                        "acceleration y": acY,
                        "acceleration z": acZ,
                        "gyroscope x": gyX,
                        "gyroscope y": gyY,
                        "gyroscope z": gyZ,
                        "magnetomete x": mgX,
                        "magnetomete y": mgY,
                        "magnetomete z": mgZ,
                        "orientation w": oriW,
                        "orientation x": oriX,
                        "orientation y": oriY,
                        "orientation z": oriZ,
                        "gravity x": gX,
                        "gravity y": gY,
                        "gravity z": gZ,
                        "linear acceleration x": linX,
                        "linear acceleration y": linY,
                        "linear acceleration z": linZ,
                        "pressure": pre,
                        "altitude": alt,
                        "temp": temp
                    }
                })

            # write after each file is read. Don't wait till all files are put in
            # json body, may not have enough ram to hold all of data
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()


def APIParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in API_BODY_PARTS:
            # get body part to add as tag for all data points in this file
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    # some of the features may be NaN values
                    features = line.split(' ')
                    # time in ms
                    ti = features[0]
                    # ignored 1 and 2, indicated by documentation
                    still_confidence = features[3]
                    on_foot_confidence = features[4]
                    walking_confidence = features[5]
                    running_confidence = features[6]
                    on_bicycle_confidence = features[7]
                    in_vehicle_confidence = features[8]
                    tilting_confidence = features[9]
                    unknown_confidence = features[10]

                    json_body.append({
                        "measurement": "API",
                        "tags": {
                            "user": user_id,
                            "body part": body_part
                        },
                        "time": ti,
                        "fields": {
                            "still confidence": still_confidence,
                            "on foot confidence": on_foot_confidence,
                            "walking confidence": walking_confidence,
                            "running confidence": running_confidence,
                            "on bicycle confidence": on_bicycle_confidence,
                            "in vehicle confidence": in_vehicle_confidence,
                            "tilting confidence": tilting_confidence,
                            "unknown confidence": unknown_confidence
                        }
                    })

            # write after each file is read. Don't wait till all files are put in
            # json body, may not have enough ram to hold all of data
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()

# this one handles variable length column data
def GPSParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in GPS_BODY_PARTS:
            # get body part to add as tag for all data points in this file
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    # some of the features may be NaN values
                    features = line.split(' ')
                    # time in ms
                    ti = features[0]
                    if len(features) == 4: # no visible satellite found
                        json_body.append({
                            "measurement": "GPS",
                            "tags": {
                                "user": user_id,
                                "body part": body_part
                            },
                            "time": ti,
                            "fields": {
                                "satellite id": 0,
                                "snr": 0,
                                "azimuth": 0,
                                "elevation": 0
                            }
                        })

                    else:
                        # add all satellites found as separate data points at same time
                        rest_features = features[3:]
                        for i in range(0, len(rest_features), 4):
                            json_body.append({
                                "measurement": "GPS",
                                "tags": {
                                    "user": user_id,
                                    "body part": body_part
                                },
                                "time": ti,
                                "fields": {
                                    "satellite id": rest_features[i],
                                    "snr": rest_features[i+1],
                                    "azimuth": rest_features[i+2],
                                    "elevation": rest_features[i+3]
                                }
                            })

            # write after each file is read. Don't wait till all files are put in
            # json body, may not have enough ram to hold all of data
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()
