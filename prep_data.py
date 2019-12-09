# will be putting loading code here
from influxdb import InfluxDBClient

db_name = 'sensor_db'

# class labels
# Null=0, Still=1, Walking=2, Run=3, Bike=4, Car=5, Bus=6, Train=7, Subway=8 

def load_data(client_db):

    # get labels with times
    # query_str += 'SELECT coarse, time '
    # query_str += 'FROM Label where time >=' 
    # query_str += 'GROUP BY "user"'
    # results = client_db.query(query_str)
    # points = results.get_points(tags={'user': '1'})
    
    # ok i got some stuff figured out
    # query_str = 'SELECT coarse '
    # query_str += "FROM Label WHERE time >= '2017-07-03 09:30:00' and time <= '2017-07-03 09:30:02' "
    # query_str += 'GROUP BY "user"'
    query_str = 'SELECT coarse '
    query_str += "FROM Label WHERE coarse=1 "
    query_str += 'GROUP BY "user"'
    results = client_db.query(query_str)
    # print(results.raw)
    points_u1 = results.get_points(tags={'user': '1'})
    points_u2 = results.get_points(tags={'user': '2'})
    points_u3 = results.get_points(tags={'user': '3'})
    # for point in points:
    #     print(point['max'])
    del results
    # get features for labels
    # results = client.query('SELECT MAX("acX"), MAX("pressure"), MAX("altitude"), MAX("temp"),'
    #                            'MIN("acX"), MIN("pressure"), MIN("altitude"), MIN("temp"),'
    #                            'MEAN("acX"), MEAN("pressure"), MEAN("altitude"), MEAN("temp"), '
    #                            'STDDEV("acX"), STDDEV("pressure"), STDDEV("altitude"), STDDEV("temp"),'
    #                            'COUNT("acX"), COUNT("pressure"), COUNT("altitude"), COUNT("temp")'
    #                            'FROM Motion WHERE time >= %ss and time <= %ss GROUP BY "user"' % (start_time, end_time))

    # points = results.get_points(tags={'user': '1'})
    # points2 = results.get_points(tags={'user': '2'})
    # points3 = results.get_points(tags={'user': '3'})
    return "ha"

if __name__ == '__main__':
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database(db_name)

    data = load_data(client)