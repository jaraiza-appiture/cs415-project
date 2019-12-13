import matplotlib.pyplot as plt
import re
import sys

client = InfluxDBClient(host='localhost', port=8086)
dblist = client.get_list_database()

#filter takes a dictionary with the following params:
#database, [name of database]
#user, [user names]
#frequency, parameter to measure
#parameter name, [parameter value to include, ! for exclude]
def filterData(filter):
    foundList
    frequency = []
    time = []
    for db in dblist:
        if db['name'] == database:
            foundList = db

    #query database for list of values corresponding to parameters
        #if filter[user] == all or filter[user] has no entry
            #query for data from all users
    for lib in foundList:
        if lib['tags']['user'] not in filter['user']:
            del foundList[lib]

    for parameters in filter['parameter name']:
        for lib in foundList:
            if lib['fields'][parameters] not in filter[parameters]:
                del foundList[lib]

    for lib in foundList:
        frequency.append(lib['fields'][filter['frequency']])
        frequency.append(lib['time'])

    #load array of xVal into xAxis, do the same for yAxis
    createGraph(frequency, time, filter['frequency])

def createGraph(frequency, time, paramName):
    #frequency is array of all the values
    xAxis = frequency
    #time is array of times corresponding to the value
    yAxis = time
    titleDefault = ' vs. Time'

    #Create graph
    plt.plot(xAxis, yAxis)
    plt.xlabel(paramName)
    plt.ylabel('Time')
    plt.title(paramName + titleDefault)
    plt.show()




