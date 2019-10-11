USER_1 = '../data/text_files/'
USER_2 = '../data_2/text_files/'
USER_3 = '../data_3/text_files/'
#not done

#dont actually think we need infParser so didnt finish it. Might need to finish if we need it but I dont think we do
def infParser():
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')

    f = open('00inf.txt','r')
    lines = f.readlines()
    userid = lines[0].split(' ')[1]
    timesmin = lines[1].split(' ')[1]
    timesmax = lines[2].split(' ')[1]
    starttime = lines[3].split(' ')[1]
    startdate = lines[3].split(' ')[2]
    millength = lines[4].split(' ')[1]
    recordId = lines[5].split(' ')[1]

def ambientParser(client):
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')
    f=open('Bag_Ambient.txt','r')

    for line in f:
        time,ign1,ign2,lumix,temp,ign3 = line.split(' ')

    data = {"measurement":"ambient",
            "tags":{"user":1},
            "time": time,
            "fields":{"lumix":lumix,
                      "temperature":temp}
            }

def batteryParser(client):
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')
    f=open('Bag_Battery.txt','r')

    for line in f:
        time,ign1,ign2,blevel,temp = line.split(' ')

    data = {"measurement":"battery",
            "tags":{"user":1},
            "time":time,
            "fields":{"battery level":blevel,
                      "temperature":temp}
            }

#tried labelstrack main but not exactly sure how we store start/end run time in db. I just chose start with end as field
def labelstrackmain():
    json_body = []
    # f = open(USER_1 + '00inf.txt', 'r')
    f=open('labels_track_main.txt','r')

    for line in f:
        starttime,endtime,activity = line.split(' ')

    data = {"measurement":"labelstrackmain",
            "tags":{"user":1},
            "time":starttime,
            "fields":{"end time":endtime,
                      "activity":activity}
            }
