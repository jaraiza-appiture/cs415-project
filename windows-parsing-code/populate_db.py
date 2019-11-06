# Usage: python3 populate_db.py

from Motion_API_GPS_parser import MotionParser, APIParser, GPSParser
from Wifi_DeprCells_parser import WifiParser, DeprCellsParser
from Ambient_Battery_Location_Label_parser import AmbientParser, BatteryParser, LocationParser, LabelParser
from influxdb import InfluxDBClient

DB_NAME = 'sensor_db'

if __name__ == '__main__':
    # connect to influxdb service
    client = InfluxDBClient(host='localhost', port=8086)
    
    if DB_NAME not in [item['name'] for item in client.get_list_database()]:
        print('Creating')
        client.create_database(DB_NAME)

    #switch to database
    client.switch_database(DB_NAME)
    
    # populate database

    print('Dropping Battery')
    client.drop_measurement('Battery')
    print('Parsing Battery')
    BatteryParser(client)

    print('Dropping Motion')
    client.drop_measurement('Motion')
    print('Parsing Motion')
    MotionParser(client)

    print('Dropping API')
    client.drop_measurement('API')
    print('Parsing API')
    APIParser(client)

    print('Dropping GPS')
    client.drop_measurement('GPS')
    print('Parsing GPS')
    GPSParser(client)

    print('Dropping WiFi')
    client.drop_measurement('WiFi')
    print('Parsing WiFi')
    WifiParser(client)

    print('Dropping DeprCells')
    client.drop_measurement('DeprCells')
    print('Parsing DeprCells')
    DeprCellsParser(client)

    print('Dropping Ambient')
    client.drop_measurement('Ambient')
    print('Parsing Ambient')
    AmbientParser(client)

    print('Dropping Location')
    client.drop_measurement('Location')
    print('Parsing Location')
    LocationParser(client)

    print('Dropping Labels')
    client.drop_measurement('Label')
    print('Parsing Labels')
    LabelParser(client)
