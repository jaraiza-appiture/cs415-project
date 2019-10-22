#Each of these parsers takes the open file and runs them through to get the data
#They each return a list of dictionaries

#The info for cells doesn't seem correct
#Number of columns in the last part doesn't match up with columns in text file
def cellParse(file):
    lteEntry = ["Cell Type","Signal Level", "Signal Strength",
                "Signal Level","Cell Identity", "Location Area Code",
                "Mobile Country Code","Mobile Network Code",
                "Physical Cell ID", "Tracking Area Code", "level"]
    gsmEntry = ["Cell Type", "Signal Level","Signal Strength",
                "Signal Level","Cell Identity", "Location Area Code",
                "Mobile Country Code", "Mobile Network Code", "level"]
    wcdmaEntry = ["Cell Type", "isRegistered","Cell Identity",
                  "Location Area Code","Mobile Country Code",
                  "Mobile Network Code","PSC","asuLevel","dBm",
                  "level"]
    i = 0
    cellList = []
    cellEntry = {} #for actual cell
    cellType = {} #for variable field
    cellEntryList = [] #for multiple entries of variable field
    line = file.readline()
    while line:
        data = line.split()
        if len(data) >= 4:
            cellEntry["Time"] = data[0]
            cellEntry["Number of Entries"] = data[3]
            i = 4
            while i < len(data):#skips if number of entries in data array is 4 (no cell entries)
                if data[i] == "WCDMA":
                    for x in range(i, i+10):
                        cellType[wcdmaEntry[x-i]] = data[x]
                    i += 10
                    cellEntryList.append(cellType)
                    cellType.clear()
                elif data[i] == "GSM":
                    for x in range(i, i+9):
                        cellType[gsmEntry[x - i]] = data[x]
                    i+=9
                    cellEntryList.append(cellType)
                    cellType.clear()
                elif data[i] == "LTE":
                    for x in range(i, i+10):
                        cellType[lteEntry[x - i]] = data[x]
                    i+=9
                    cellEntryList.append(cellType)
                    cellType.clear() #ski
            cellEntry["Cell Entry List"] = cellEntryList
            cellEntryList.clear()
        cellList.append(cellEntry)
        line = file.readline()
    return cellList

def locationParse(file):
    locationList = []
    locationEntry = {}
    line = file.readline()
    while line:
        data = line.split()
        locationEntry["Time"] = data[0]
        locationEntry["Accuracy"] = data[3]
        locationEntry["Latitude"] = data[4]
        locationEntry["Longitude"] = data[5]
        locationEntry["Altitude"] = data[6]
        locationList.append(locationEntry)
        locationEntry.clear()
        line = file.readline
    return locationList

def labelParse(file):
    coarseLabel = {
        "0":"Null",
        "1":"Still",
        "2":"Walking",
        "3":"Running",
        "4":"Biking",
        "5":"Car",
        "6":"Bus",
        "7":"Train",
        "8":"Subway"
    }
    fineLabel = {
    "0":"Null",
    "1":"Still;Stand;Outside",
    "2":"Still;Stand;Inside",
    "3":"Still;Sit;Outside",
    "4":"Still;Sit;Inside",
    "5":"Walking;Outside",
    "6":"Walking;Inside",
    "7":"Run",
    "8":"Bike",
    "9":"Car;Driver",
    "10":"Car;Passenger",
    "11":"Bus;Stand",
    "12":"Bus;Sit",
    "13":"Bus;Up;Stand",
    "14":"Bus;Up;Sit",
    "15":"Train;Stand",
    "16":"Train;Sit",
    "17":"Subway;Stand",
    "18":"Subway;Sit",
    }
    roadLabel = {
        "0":"Null",
        "1":"City",
        "2":"Motorway",
        "3":"Countryside",
        "4":"Dirt Road"
    }
    trafficLabel = {"0":"Null","1":"Heavy Traffic"}
    tunnelLabel = {"0":"Null","1":"Tunnel"}
    socialLabel = {"0":"Null","1":"Social"}
    foodLabel = {"0":"Null", "1":"Eating","2":"Drinking","3":"Both"}
    labelList = []
    labelEntry = {}
    line = file.readline()
    while line():
        data = line.split()
        labelEntry["Time"] = data[0]
        labelEntry["Course"] = coarseLabel[data[1]]
        labelEntry["Fine"] = fineLabel[data[2]]
        labelEntry["Road"] = roadLabel[data[3]]
        labelEntry["Traffic"] = trafficLabel[data[4]]
        labelEntry["Tunnel"] = tunnelLabel[data[5]]
        labelEntry["Social"] = socialLabel[data[6]]
        labelEntry["Food"] = foodLabel[data[7]]
        labelList.append(labelEntry)
        labelEntry.clear()
        line = file.readline()
    return labelList



def cellParser(client):
    json_body = []
    result = []
    for user_file, user_id in USERS:
        for body_part_file in MOTION_BODY_PARTS:
            with open(user_file + body_part_file, 'r') as inFile:
                result = cellParse(inFile)
                for x in result:
                    time = x["Time"]
                    del x["Time"]
                    json_body.append({
                        "measurement":"Cell",
                        "tags": {
                            "user": user_id,
                            "body part": body_part
                        },
                        "fields":x
                    })
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()

def locationParser(client):
    json_body = []
    result = []
    for user_file, user_id in USERS:
        for body_part_file in MOTION_BODY_PARTS:
            with open(user_file + body_part_file, 'r') as inFile:
                result = locationParse(inFile)
                for x in result:
                    time = x["Time"]
                    del x["Time"]
                    json_body.append({
                        "measurement":"Cell",
                        "tags": {
                            "user": user_id,
                            "body part": body_part
                        },
                        "fields":x
                    })
            if not client.write_points(json_body):
                print('Failed to write to database!')
            json_body.clear()

def labelParser(client):
    json_body = []
    result = []
    for user_file, user_id in USERS:
        with open(user_file + body_part_file, 'r') as inFile:
            result = labelParse(inFile)
            for x in result:
                time = x["Time"]
                del x["Time"]
                json_body.append({
                    "measurement":"Cell",
                    "tags": {
                        "user": user_id
                    },
                    "fields":x
                })
        if not client.write_points(json_body):
            print('Failed to write to database!')
        json_body.clear()