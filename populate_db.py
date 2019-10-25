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
    if DB_NAME in [item['name'] for item in client.get_list_database()]:
        client.drop_database(DB_NAME)

    client.create_database(DB_NAME)
    # switch to database
    client.switch_database(DB_NAME)
    # populate database
    MotionParser(client)
    APIParser(client)
    GPSParser(client)
    WifiParser(client)
    DeprCellsParser(client)
    AmbientParser(client)
    BatteryParser(client)
    LocationParser(client)
    LabelParser(client)