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

def call_wifi(client, start_time = None, end_time = None):
    if start_time == None or end_time == None:
        results = client.query('SELECT MAX("frequency"), '
                               'MIN("frequency"),'
                               'MEAN("frequency"),'
                               'STDDEV("frequency"),'
                               'COUNT("frequency")'
                               ' FROM WiFi GROUP BY "user"')

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max frequency: %s" % (point['max']))
        print("Min frequency: %s" % (point['min']))
        print("Mean frequency: %s" % (point['mean']))
        print("STDDEV frequency: %s" % (point['stddev']))
        print("Count frequency: %s\n" % (point['count']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max frequency: %s" % (point['max']))
        print("Min frequency: %s" % (point['min']))
        print("Mean frequency: %s" % (point['mean']))
        print("STDDEV frequency: %s" % (point['stddev']))
        print("Count frequency: %s\n" % (point['count']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max frequency: %s" % (point['max']))
        print("Min frequency: %s" % (point['min']))
        print("Mean frequency: %s" % (point['mean']))
        print("STDDEV frequency: %s" % (point['stddev']))
        print("Count frequency: %s\n" % (point['count']))

def call_GPS(client, start_time = None, end_time = None):
    if start_time == None or end_time == None:
        results = client.query('SELECT MAX("snr"), MAX("azimuth"), MAX("elevation"),'
                               'MIN("snr"), MIN("azimuth"), MIN("elevation"),'
                               'MEAN("snr"), MEAN("azimuth"), MEAN("elevation"),'
                               'STDDEV("snr"), STDDEV("azimuth"), STDDEV("elevation"),'
                               'COUNT("snr"), COUNT("azimuth"), COUNT("elevation")'
                               ' FROM GPS GROUP BY "user"')

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max snr: %s, Max azimuth: %s, Max elevation: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min snr: %s, Min azimuth: %s, Min elevation: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean snr: %s, Mean azimuth: %s, Mean elevation: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV snr: %s, STDDEV azimuth: %s, STDDEV elevation: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT snr: %s, COUNT azimuth: %s, Count elevation: %s\n" % (point['count'], point['count_1'], point['count_2']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max snr: %s, Max azimuth: %s, Max elevation: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min snr: %s, Min azimuth: %s, Min elevation: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean snr: %s, Mean azimuth: %s, Mean elevation: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV snr: %s, STDDEV azimuth: %s, STDDEV elevation: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT snr: %s, COUNT azimuth: %s, Count elevation: %s\n" % (point['count'], point['count_1'], point['count_2']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max snr: %s, Max azimuth: %s, Max elevation: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min snr: %s, Min azimuth: %s, Min elevation: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean snr: %s, Mean azimuth: %s, Mean elevation: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV snr: %s, STDDEV azimuth: %s, STDDEV elevation: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT snr: %s, COUNT azimuth: %s, Count elevation: %s\n" % (point['count'], point['count_1'], point['count_2']))

def call_motion(client, start_time = None, end_time = None):
    if start_time == None or end_time == None:
        results = client.query('SELECT MAX("acX"), MAX("pressure"), MAX("altitude"), MAX("temp"),'
                               'MIN("acX"), MIN("pressure"), MIN("altitude"), MIN("temp"),'
                               'MEAN("acX"), MEAN("pressure"), MEAN("altitude"), MEAN("temp"), '
                               'STDDEV("acX"), STDDEV("pressure"), STDDEV("altitude"), STDDEV("temp"),'
                               'COUNT("acX"), COUNT("pressure"), COUNT("altitude"), COUNT("temp")'
                               ' FROM Motion GROUP BY "user"')

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max acX: %s, Max pressure: %s, Max altitude: %s, Max temp: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min acX: %s, Min pressure: %s, Min altitude: %s, Min temp: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean acX: %s, Mean pressure: %s, Mean altitude: %s, Mean temp: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV acX: %s, STDDEV pressure: %s, STDDEV altitude: %s, STDDEV temp: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count acX: %s, Count pressure: %s, Count altitude: %s, Count temp: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max acX: %s, Max pressure: %s, Max altitude: %s, Max temp: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min acX: %s, Min pressure: %s, Min altitude: %s, Min temp: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean acX: %s, Mean pressure: %s, Mean altitude: %s, Mean temp: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV acX: %s, STDDEV pressure: %s, STDDEV altitude: %s, STDDEV temp: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count acX: %s, Count pressure: %s, Count altitude: %s, Count temp: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max acX: %s, Max pressure: %s, Max altitude: %s, Max temp: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min acX: %s, Min pressure: %s, Min altitude: %s, Min temp: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean acX: %s, Mean pressure: %s, Mean altitude: %s, Mean temp: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV acX: %s, STDDEV pressure: %s, STDDEV altitude: %s, STDDEV temp: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count acX: %s, Count pressure: %s, Count altitude: %s, Count temp: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))

def call_label(client, start_time = None, end_time = None):
    if start_time == None and end_time == None:
        results = client.query('SELECT MAX("coarse"), MAX("fine"), '
                               'MIN("coarse"), MIN("fine"),'
                               'MEAN("coarse"), MEAN("fine"),'
                               'STDDEV("coarse"), STDDEV("fine"),'
                               'COUNT("coarse"), COUNT("fine")'
                               ' FROM Label GROUP BY "user"')

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max coarse: %s, Max fine: %s" % (point['max'], point['max_1']))
        print("Min coarse: %s, Min fine: %s" % (point['min'], point['min_1']))
        print("Mean coarse: %s, Mean fine: %s" % (point['mean'], point['mean_1']))
        print("STDDEV coarse: %s, STDDEV fine: %s" % (point['stddev'], point['stddev_1']))
        print("Count coarse: %s, Count fine: %s\n" % (point['count'], point['count_1']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max coarse: %s, Max fine: %s" % (point['max'], point['max_1']))
        print("Min coarse: %s, Min fine: %s" % (point['min'], point['min_1']))
        print("Mean coarse: %s, Mean fine: %s" % (point['mean'], point['mean_1']))
        print("STDDEV coarse: %s, STDDEV fine: %s" % (point['stddev'], point['stddev_1']))
        print("Count coarse: %s, Count fine: %s\n" % (point['count'], point['count_1']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max coarse: %s, Max fine: %s" % (point['max'], point['max_1']))
        print("Min coarse: %s, Min fine: %s" % (point['min'], point['min_1']))
        print("Mean coarse: %s, Mean fine: %s" % (point['mean'], point['mean_1']))
        print("STDDEV coarse: %s, STDDEV fine: %s" % (point['stddev'], point['stddev_1']))
        print("Count coarse: %s, Count fine: %s\n" % (point['count'], point['count_1']))

def call_location(client, start_time = None, end_time = None):
    if start_time == None or end_time == None:
        results = client.query('SELECT MAX("accuracy"), MAX("latitude"), MAX("longitude"), MAX("altitude"),'
                               'MIN("accuracy"), MIN("latitude"), MIN("longitude"), MIN("altitude"),'
                               'MEAN("accuracy"), MEAN("latitude"), MEAN("longitude"), MEAN("altitude"), '
                               'STDDEV("accuracy"), STDDEV("latitude"), STDDEV("longitude"), STDDEV("altitude"),'
                               'COUNT("accuracy"), COUNT("latitude"), COUNT("longitude"), COUNT("altitude")'
                               ' FROM Location GROUP BY "user"')
    else:
        pass

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max accuracy: %s, Max latitude: %s, Max longitude: %s, Max altitude: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min accuracy: %s, Min latitude: %s, Min longitude: %s, Min altitude: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean accuracy: %s, Mean latitude: %s, Mean longitude: %s, Mean altitude: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV accuracy: %s, STDDEV latitude: %s, STDDEV longitude: %s, STDDEV altitude: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count accuracy: %s, Count latitude: %s, Count longitude: %s, Count altitude: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max accuracy: %s, Max latitude: %s, Max longitude: %s, Max altitude: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min accuracy: %s, Min latitude: %s, Min longitude: %s, Min altitude: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean accuracy: %s, Mean latitude: %s, Mean longitude: %s, Mean altitude: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV accuracy: %s, STDDEV latitude: %s, STDDEV longitude: %s, STDDEV altitude: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count accuracy: %s, Count latitude: %s, Count longitude: %s, Count altitude: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max accuracy: %s, Max latitude: %s, Max longitude: %s, Max altitude: %s" % (point['max'], point['max_1'], point['max_2'], point['max_3']))
        print("Min accuracy: %s, Min latitude: %s, Min longitude: %s, Min altitude: %s" % (point['min'], point['min_1'], point['min_2'], point['min_3']))
        print("Mean accuracy: %s, Mean latitude: %s, Mean longitude: %s, Mean altitude: %s" % (point['mean'], point['mean_1'], point['mean_2'], point['mean_3']))
        print("STDDEV accuracy: %s, STDDEV latitude: %s, STDDEV longitude: %s, STDDEV altitude: %s" % (point['stddev'], point['stddev_1'], point['stddev_2'], point['stddev_3']))
        print("Count accuracy: %s, Count latitude: %s, Count longitude: %s, Count altitude: %s\n" % (point['count'], point['count_1'], point['count_2'], point['count_3']))

def call_API(client, start_time = None, end_time = None):
    if start_time == None or end_time == None:
        results = client.query('SELECT MAX("still confidence"), MAX("on foot confidence"), MAX("walking confidence"),'
                               'MIN("still confidence"), MIN("on foot confidence"), MIN("walking confidence"),'
                               'MEAN("still confidence"), MEAN("on foot confidence"), MEAN("walking confidence"),'
                               'STDDEV("still confidence"), STDDEV("on foot confidence"), STDDEV("walking confidence"),'
                               'COUNT("still confidence"), COUNT("on foot confidence"), COUNT("walking confidence")'
                               ' FROM API GROUP BY "user"')
    else:
        results = client.query('SELECT MAX("still confidence"), MAX("on foot confidence"), MAX("walking confidence"),'
                               'MIN("still confidence"), MIN("on foot confidence"), MIN("walking confidence"),'
                               'MEAN("still confidence"), MEAN("on foot confidence"), MEAN("walking confidence"),'
                               'STDDEV("still confidence"), STDDEV("on foot confidence"), STDDEV("walking confidence"),'
                               'COUNT("still confidence"), COUNT("on foot confidence"), COUNT("walking confidence")'
                               ' FROM API GROUP BY "user" where time >= "%s" and time <= "%s"', start_time, end_time)

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max still confidence: %s, Max foot confidence: %s, Max walking confidence: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min still confidence: %s, Min foot confidence: %s, Min walking confidence: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean still confidence: %s, Mean foot confidence: %s, Mean walking confidence: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV still confidence: %s, STDDEV foot confidence: %s, STDDEV walking confidence: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT still confidence: %s, COUNT foot confidence: %s, Count walking confidence: %s\n" % (point['count'], point['count_1'], point['count_2']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max still confidence: %s, Max foot confidence: %s, Max walking confidence: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min still confidence: %s, Min foot confidence: %s, Min walking confidence: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean still confidence: %s, Mean foot confidence: %s, Mean walking confidence: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV still confidence: %s, STDDEV foot confidence: %s, STDDEV walking confidence: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT still confidence: %s, COUNT foot confidence: %s, Count walking confidence: %s\n" % (point['count'], point['count_1'], point['count_2']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max still confidence: %s, Max foot confidence: %s, Max walking confidence: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min still confidence: %s, Min foot confidence: %s, Min walking confidence: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean still confidence: %s, Mean foot confidence: %s, Mean walking confidence: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV still confidence: %s, STDDEV foot confidence: %s, STDDEV walking confidence: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT still confidence: %s, COUNT foot confidence: %s, Count walking confidence: %s\n" % (point['count'], point['count_1'], point['count_2']))

def call_ambient(client, start_time = None, end_time = None):
    if start_time == None and end_time == None:
        results = client.query('SELECT MAX("temperature"), MAX("lumix"), '
                               'MIN("temperature"), MIN("lumix"),'
                               'MEAN("temperature"), MEAN("lumix"),'
                               'STDDEV("temperature"), STDDEV("lumix"),'
                               'COUNT("temperature"), COUNT("lumix")'
                               ' FROM Ambient GROUP BY "user"')
    else:
        results = client.query('SELECT MAX("temperature"), MAX("lumix"), '
                               'MIN("temperature"), MIN("lumix"),'
                               'MEAN("temperature"), MEAN("lumix"),'
                               'STDDEV("temperature"), STDDEV("lumix"),'
                               'COUNT("temperature"), COUNT("lumix")'
                               ' FROM Ambient GROUP BY "user" where time >= "%s" and time <= "%s"', start_time,
                               end_time)

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max temperature: %s, Max lumix: %s" % (point['max'], point['max_1']))
        print("Min temperature: %s, Min lumix: %s" % (point['min'], point['min_1']))
        print("Mean temperature: %s, Mean lumix: %s" % (point['mean'], point['mean_1']))
        print("STDDEV temperature: %s, STDDEV lumix: %s" % (point['stddev'], point['stddev_1']))
        print("Count temperature: %s, Count lumix: %s\n" % (point['count'], point['count_1']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max temperature: %s, Max lumix: %s" % (point['max'], point['max_1']))
        print("Min temperature: %s, Min lumix: %s" % (point['min'], point['min_1']))
        print("Mean temperature: %s, Mean lumix: %s" % (point['mean'], point['mean_1']))
        print("STDDEV temperature: %s, STDDEV lumix: %s" % (point['stddev'], point['stddev_1']))
        print("Count temperature: %s, Count lumix: %s\n" % (point['count'], point['count_1']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max temperature: %s, Max lumix: %s" % (point['max'], point['max_1']))
        print("Min temperature: %s, Min lumix: %s" % (point['min'], point['min_1']))
        print("Mean temperature: %s, Mean lumix: %s" % (point['mean'], point['mean_1']))
        print("STDDEV temperature: %s, STDDEV lumix: %s" % (point['stddev'], point['stddev_1']))
        print("Count temperature: %s, Count lumix: %s\n" % (point['count'], point['count_1']))

def call_battery(client, start_time = None, end_time = None):
    if start_time == None and end_time == None:
        results = client.query('SELECT MAX("battery level"), MAX("temperature"), '
                               'MIN("battery level"), MIN("temperature"),'
                               'MEAN("battery level"), MEAN("temperature"),'
                               'STDDEV("battery level"), STDDEV("temperature"),'
                               'COUNT("battery level"), COUNT("temperature")'
                               ' FROM Battery GROUP BY "user"')
    else:
        results = client.query('SELECT MAX("battery level"), MAX("temperature"), '
                               'MIN("battery level"), MIN("temperature"),'
                               'MEAN("battery level"), MEAN("temperature"),'
                               'STDDEV("battery level"), STDDEV("temperature"),'
                               'COUNT("battery level"), COUNT("temperature")'
                               ' FROM Battery GROUP BY "user" where time >= "%s" and time <= "%s"', start_time, end_time)

    #print(results.raw)

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    # points = results.get_points()

    print("User 1 statistics: ")
    for point in points:
        print("Max battery level: %s, Max temperature: %s" % (point['max'], point['max_1']))
        print("Min battery level: %s, Min temperature: %s" % (point['min'], point['min_1']))
        print("Mean battery level: %s, Mean temperature: %s" % (point['mean'], point['mean_1']))
        print("STDDEV battery level: %s, STDDEV temperature: %s" % (point['stddev'], point['stddev_1']))
        print("Count battery level: %s, Count temperature: %s\n" % (point['count'], point['count_1']))
    print("User 2 statistics: ")
    for point in points2:
        print("Max battery level: %s, Max temperature: %s" % (point['max'], point['max_1']))
        print("Min battery level: %s, Min temperature: %s" % (point['min'], point['min_1']))
        print("Mean battery level: %s, Mean temperature: %s" % (point['mean'], point['mean_1']))
        print("STDDEV battery level: %s, STDDEV temperature: %s" % (point['stddev'], point['stddev_1']))
        print("Count battery level: %s, Count temperature: %s\n" % (point['count'], point['count_1']))
    print("User 3 statistics: ")
    for point in points3:
        print("Max battery level: %s, Max temperature: %s" % (point['max'], point['max_1']))
        print("Min battery level: %s, Min temperature: %s" % (point['min'], point['min_1']))
        print("Mean battery level: %s, Mean temperature: %s" % (point['mean'], point['mean_1']))
        print("STDDEV battery level: %s, STDDEV temperature: %s" % (point['stddev'], point['stddev_1']))
        print("Count battery level: %s, Count temperature: %s\n" % (point['count'], point['count_1']))


def call_depr_cells(client, start_time = None, end_time = None):
    if start_time == None and end_time == None:
        results = client.query('SELECT MAX("network type"), MAX("cid"), MAX("lac"),'
                               'MIN("network type"), MIN("cid"), MIN("lac"),'
                               'MEAN("network type"), MEAN("cid"), MEAN("lac"),'
                               'STDDEV("network type"), STDDEV("cid"), STDDEV("lac"),'
                               'COUNT("network type"), COUNT("cid"), COUNT("lac")'
                               ' FROM DeprCells GROUP BY "user"')
    else:
        results = client.query('SELECT MAX("network type"), MAX("cid"), MAX("lac"),'
                               'MIN("network type"), MIN("cid"), MIN("lac"),'
                               'MEAN("network type"), MEAN("cid"), MEAN("lac"),'
                               'STDDEV("network type"), STDDEV("cid"), STDDEV("lac"),'
                               'COUNT("network type"), COUNT("cid"), COUNT("lac")'
                               ' FROM DeprCells GROUP BY "user" where time >= "%s" and time <= "%s"', start_time,
                               end_time)

    points = results.get_points(tags={'user': '1'})
    points2 = results.get_points(tags={'user': '2'})
    points3 = results.get_points(tags={'user': '3'})

    print("User 1 statistics: ")
    for point in points:
        print("Max network: %s, Max cid: %s, Max lac: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min network: %s, Min cid: %s, Min lac: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean network: %s, Mean cid: %s, Mean lac: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV network: %s, STDDEV cid: %s, STDDEV lac: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT network: %s, COUNT cid: %s, Count lac: %s\n" % (point['count'], point['count_1'], point['count_2']))

    print("User 2 statistics: ")
    for point in points2:
        print("Max network: %s, Max cid: %s, Max lac: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min network: %s, Min cid: %s, Min lac: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean network: %s, Mean cid: %s, Mean lac: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV network: %s, STDDEV cid: %s, STDDEV lac: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT network: %s, COUNT cid: %s, Count lac: %s\n" % (point['count'], point['count_1'], point['count_2']))

    print("User 3 statistics: ")
    for point in points3:
        print("Max network: %s, Max cid: %s, Max lac: %s" % (point['max'], point['max_1'], point['max_2']))
        print("Min network: %s, Min cid: %s, Min lac: %s" % (point['min'], point['min_1'], point['min_2']))
        print("Mean network: %s, Mean cid: %s, Mean lac: %s" % (point['mean'], point['mean_1'], point['mean_2']))
        print("STDDEV network: %s, STDDEV cid: %s, STDDEV lac: %s" % (point['stddev'], point['stddev_1'], point['stddev_2']))
        print("COUNT network: %s, COUNT cid: %s, Count lac: %s\n" % (point['count'], point['count_1'], point['count_2']))

option = -1

while option != '0':
    option = input("Would you like to query data by:\n 1. Time or \n 2. Sensor Type\n")

    if option == '1':
        start_time = input("\nEnter the start time: ")
        end_time = input("\nEnter the end time: ")

        call_battery(client, start_time, end_time)

    if option == '2':
        print("\nThe sensor types are: API, Ambient, Battery, DeprCells, GPS, Label, Location, Motion, WiFi.\n")
        sensor_type = input("Enter the name of the sensor you would like to see the statistics of: ")

        if sensor_type == "Battery":
            call_battery(client)

        if sensor_type == "Ambient":
            call_ambient(client)

        if sensor_type == "API":
            call_API(client)

        if sensor_type == "DeprCells":
            call_depr_cells(client)

        if sensor_type == "GPS":
            call_GPS(client)

        if sensor_type == "Label":
            call_label(client)

        if sensor_type == "Location":
            call_location(client)

        if sensor_type == "Motion":
            call_motion(client)

        if sensor_type == "Wifi":
            call_wifi(client)
