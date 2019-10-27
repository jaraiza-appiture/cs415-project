# Usage: python3 populate_db.py

from Motion_API_GPS_parser import MotionParser, APIParser, GPSParser
from Wifi_DeprCells_parser import WifiParser, DeprCellsParser
from Ambient_Battery_Location_Label_parser import AmbientParser, BatteryParser, LocationParser, LabelParser
from influxdb import InfluxDBClient

DB_NAME = 'sensor_db'

if __name__ == '__main__':
    # connect to influxdb service
    client = InfluxDBClient(host='localhost', port=8086)
    # if already exists, then we must be re-populating so drop it
    # if DB_NAME in [item['name'] for item in client.get_list_database()]:
    #     print('Dropping')
    #     client.drop_database(DB_NAME)
    # print('Creating')
    # client.create_database(DB_NAME)
    # switch to database
    client.switch_database(DB_NAME)
    
    # populate database
    # print('Parsing Motion')
    # MotionParser(client)
    
    #print('Dropping API')
    #client.drop_measurement('API')
    # print('Parsing API')
    # APIParser(client)
    
    # print('Dropping GPS')
    # client.drop_measurement('GPS')
    # print('Parsing GPS')
    # GPSParser(client)
    
    # print('Dropping WiFi')
    # client.drop_measurement('WiFi')
    # print('Parsing WiFi')
    # WifiParser(client)

    # finih deprCell
    print('Dropping DeprCells')
    client.drop_measurement('DeprCells')
    print('Parsing DeprCells')
    DeprCellsParser(client)
    
    # print('Parsing Ambient')
    # AmbientParser(client)
    
    # print('Parsing Battery')
    # BatteryParser(client)
    
    # print('Parsing Location')
    # LocationParser(client)
    
    # print('Parsing Labels')
    # LabelParser(client)