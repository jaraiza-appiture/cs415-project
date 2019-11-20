from influxdb import InfluxDBClient

db_name = 'sensor_db'

client = InfluxDBClient(host='localhost', port=8086)
dblist = client.get_list_database()
db_found = False
for db in dblist:
    if db['name'] == db_name:
        db_found = True

if not db_found:
    print("Could not find database")
else:
    print("Found the database")

client.switch_database('sensor_db')

user_1 = {
    'motion': {},
    'api': {},
    'ambient': {},
    'battery': {},
    'gps': {},
    'wifi': {},
    'depr_cells': {},
    'cells': {},
    'location': {},
    'label': {}
}

user_2 = {
    'motion': {},
    'api': {},
    'ambient': {},
    'battery': {},
    'gps': {},
    'wifi': {},
    'depr_cells': {},
    'cells': {},
    'location': {},
    'label': {}
}

user_3 = {
    'motion': {},
    'api': {},
    'ambient': {},
    'battery': {},
    'gps': {},
    'wifi': {},
    'depr_cells': {},
    'cells': {},
    'location': {},
    'label': {}
}

# API##############################################################################

results = client.query('SELECT MAX("network type"), MAX("cid"), MAX("lac"),'
                       'MIN("network type"), MIN("cid"), MIN("lac"),'
                       'MEAN("network type"), MEAN("cid"), MEAN("lac"),'
                       'STDDEV("network type"), STDDEV("cid"), STDDEV("lac"),'
                       'COUNT("network type"), COUNT("cid"), COUNT("lac")'
                       ' FROM DeprCells GROUP BY "user"')
print(results.raw)


# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# Wifi##############################################################################

# results = client.query('SELECT MAX("frequency"), '
#                        'MIN("frequency"),'
#                        'MEAN("frequency"),'
#                        'STDDEV("frequency"),'
#                        'COUNT("frequency")'
#                        ' FROM WiFi GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# GPS##############################################################################

# results = client.query('SELECT MAX("snr"), MAX("azimuth"), MAX("elevation"),'
#                        'MIN("snr"), MIN("azimuth"), MIN("elevation"),'
#                        'MEAN("snr"), MEAN("azimuth"), MEAN("elevation"),'
#                        'STDDEV("snr"), STDDEV("azimuth"), STDDEV("elevation"),'
#                        'COUNT("snr"), COUNT("azimuth"), COUNT("elevation")'
#                        ' FROM GPS GROUP BY "user"')
# print(results.raw)


# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# API##############################################################################

# results = client.query('SELECT MAX("still confidence"), MAX("on foot confidence"), MAX("walking confidence"),'
#                        'MIN("still confidence"), MIN("on foot confidence"), MIN("walking confidence"),'
#                        'MEAN("still confidence"), MEAN("on foot confidence"), MEAN("walking confidence"),'
#                        'STDDEV("still confidence"), STDDEV("on foot confidence"), STDDEV("walking confidence"),'
#                        'COUNT("still confidence"), COUNT("on foot confidence"), COUNT("walking confidence")'
#                        ' FROM API GROUP BY "user"')
# print(results.raw)


# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# not sure if works: motion##############################################################################

# results = client.query('SELECT MAX("acX"), MAX("pressure"), MAX("altitude"), MAX("temp"),'
#                        'MIN("acX"), MIN("pressure"), MIN("altitude"), MIN("temp"),'
#                        'MEAN("acX"), MEAN("pressure"), MEAN("altitude"), MEAN("temp"), '
#                        'STDDEV("acX"), STDDEV("pressure"), STDDEV("altitude"), STDDEV("temp"),'
#                        'COUNT("acX"), COUNT("pressure"), COUNT("altitude"), COUNT("temp")'
#                        ' FROM Motion GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# label##############################################################################

# results = client.query('SELECT MAX("coarse"), MAX("fine"), '
#                        'MIN("coarse"), MIN("fine"),'
#                        'MEAN("coarse"), MEAN("fine"),'
#                        'STDDEV("coarse"), STDDEV("fine"),'
#                        'COUNT("coarse"), COUNT("fine")'
#                        ' FROM Label GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################


# location##############################################################################

# results = client.query('SELECT MAX("accuracy"), MAX("latitude"), MAX("longitude"), MAX("altitude"),'
#                        'MIN("accuracy"), MIN("latitude"), MIN("longitude"), MIN("altitude"),'
#                        'MEAN("accuracy"), MEAN("latitude"), MEAN("longitude"), MEAN("altitude"), '
#                        'STDDEV("accuracy"), STDDEV("latitude"), STDDEV("longitude"), STDDEV("altitude"),'
#                        'COUNT("accuracy"), COUNT("latitude"), COUNT("longitude"), COUNT("altitude")'
#                        ' FROM Location GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################


# battery##############################################################################

# results = client.query('SELECT MAX("battery level"), MAX("temperature"), '
#                        'MIN("battery level"), MIN("temperature"),'
#                        'MEAN("battery level"), MEAN("temperature"),'
#                        'STDDEV("battery level"), STDDEV("temperature"),'
#                        'COUNT("battery level"), COUNT("temperature")'
#                        ' FROM Battery GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# ambient##############################################################################

# results = client.query('SELECT MAX("temperature"), MAX("lumix"), '
#                        'MIN("temperature"), MIN("lumix"),'
#                        'MEAN("temperature"), MEAN("lumix"),'
#                        'STDDEV("temperature"), STDDEV("lumix"),'
#                        'COUNT("temperature"), COUNT("lumix")'
#                        ' FROM Ambient GROUP BY "user"')
# print(results.raw)

# points = results.get_points(tags={'user': '1'})
# points2 = results.get_points(tags={'user':'2'})
# points3 = results.get_points(tags={'user':'3'})


##########################################################################################################

# start_time = input("\nEnter the start time: ")
# end_time = input("\nEnter the end time: ")

# def call_ambient(client, start_time = None, end_time = None):
#     pass
#
# def call_API(client, start_time = None, end_time = None):
#     pass
#
# def call_battery(client, start_time = None, end_time = None):
#     pass
#
# def call_depr_cells(client, start_time = None, end_time = None):
#     pass
#
# def call_GPS(start_time = None, end_time = None):
#     pass
#
# def call_label(start_time = None, end_time = None):
#     pass
#
# def call_location(start_time = None, end_time = None):
#     pass
#
# def call_motion(start_time = None, end_time = None):
#     pass
#
# def call_wifi(start_time = None, end_time = None):
#     pass



# option = -1
#
# while option != '0':
#     option = input("Would you like to query data by:\n 1. Time or \n 2. Sensor Type\n")
#
#     if option == '1':
#         start_time = input("\nEnter the start time: ")
#         end_time = input("\nEnter the end time: ")
    #     pass
    #
    # if option == '2':
    #     print("The sensor types are: API, Ambient, Battery, DeprCells, GPS, Label, Location, Motion, WiFi.\n")
    #     sensor_type = input("Enter the name of the sensor you would like to see the statistics of: ")
    #
    #     if sensor_type == "Ambient":
    #         #call_ambient()
    #         results = client.query('SELECT MAX("temperature") FROM ' + sensor_type + ' GROUP BY "user"')
    #         print(results.raw)
    #         points = results.get_points()
    #         for point in points:
    #             print("Time: %s, Temperature: %s" % (point['time'], point['max']))
    #
    #         results = client.query('SELECT MAX("lumix") FROM ' + sensor_type + ' GROUP BY "user"')
    #
    #     if sensor_type == "API":
    #         call_API()
    #     print("The sensor types are: API, Ambient, Battery, DeprCells, GPS, Label, Location, Motion, WiFi.\n")
    #
    #     if sensor_type == "Battery":
    #         call_battery()
    #
    #     if sensor_type == "DeprCells":
    #         call_depr_cells()
    #
    #     if sensor_type == "GPS":
    #         call_GPS()
    #
    #     if sensor_type == "Label":
    #         call_label()
    #
    #     if sensor_type == "Location":
    #         call_location()
    #
    #     if sensor_type == "Motion":
    #         call_motion()
    #
    #     if sensor_type == "Wifi":
    #         call_wifi()
