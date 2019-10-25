from constants import USERS, WIFI_BODY_PARTS, DEPRCELLS_BODY_PARTS


def WifiParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in WIFI_BODY_PARTS:
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    # file delimited by semicolon
                    features = line.split(';')
                    # time in ms
                    ti = int(features[0])
                    # ignore next 2 columns
                    data_present = features[3]
                    if data_present == 0: # no wifi data present
                        continue
                    else:
                        # add all 5 wifi fields
                        rest_features = features[4:]
                        for i in range(0, len(rest_features), 5):
                            json_body.append({
                                "measurement": "Wifi",
                                "tags": {
                                    "user": user_id,
                                    "body part": body_part,
                                    "bssid": rest_features[i]
                                },
                                "time": ti,
                                "fields": {
                                    "ssid": rest_features[i+1],
                                    "rssi": rest_features[i+2],
                                    "frequency": int(rest_features[i+3]),
                                    "capabilities": rest_features[i+4]
                                }
                            })

            if not client.write_points(json_body, time_precision='ms'):
                print('Failed to write to database!')

            json_body.clear()



def DeprCellsParser(client):
    json_body = []

    for user_file, user_id in USERS:
        for body_part_file in DEPRCELLS_BODY_PARTS:
            # get body part to add as tag for all data points in this file
            body_part = body_part_file.split('_')[0]
            with open(user_file + body_part_file, 'r') as in_file:
                for line in in_file:
                    # some of the features may be NaN values
                    features = line.split(' ')
                    # time in ms
                    ti = int(features[0])
                    # ignore 1 and 2
                    if len(features) > 3:
                        network_type = features[3]
                        cid = features[4]
                        lac = features[5]
                        dbm = features[6]
                        mcc = features[7]
                        mns = features[8]

                        json_body.append({
                            "measurement": "DeprCells",
                            "tags": {
                                "user": user_id,
                                "body part": body_part
                            },
                            "time": ti,
                            "fields": {
                                "network type": int(network_type),
                                "cid": int(cid),
                                "lac": int(lac),
                                "dbm": int(dbm),
                                "mcc": int(mcc),
                                "mns": int(mns)
                            }
                        })

            if not client.write_points(json_body, time_precision='ms'):
                print('Failed to write to database!')
            json_body.clear()
