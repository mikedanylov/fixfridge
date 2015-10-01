__author__ = 'mikedanylov'

import serial
import psycopg2


class UsbReader(object):
    """
    - opens specified serial port
    - reads port for specified interval
    - writes values to specified database
    """

    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):

        self.port = port
        self.baudrate = baudrate

        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
            f = open(self.port, 'w')

        except OSError:
            print('ERROR: Receiver is not connected!')
            print('Check for \'/dev/ttyUSBx\' device. If there is such port then do \'sudo chmod 777 /dev/ttyUSBx\'')

    def read_value(self):
        '''
        Reads one value from serial port
        Returns id and data
        '''
        line = str(self.ser.readline())
        line = line[2:-1]  # cut b' in the beginning and ' in the end
        # # debugging
        # print(line)
        # print(type(line))
        if line != '':
            line = line[:-4]  # drop \r\n
            # # debugging
            # print(line)
            sensor = line.split(',')  # split line to int id and float data
            sensor_id = int(sensor[0])
            sensor_data = float(sensor[1])
            # debugging
            print(sensor_id, sensor_data)
            return sensor_id, sensor_data
        else:
            return None, None

    def write_to_db(self, sensor_id, sensor_data):
        # Try to connect
        try:
            conn = psycopg2.connect("dbname='sensodb' user='mikedanylov' password='ps7vj590'")
            cur = conn.cursor()
            cur.execute("SET TIME ZONE 'Europe/Helsinki';")
        except:
            print('I am unable to connect to the database.')
            return 'not OK'
        try:
            cur.execute(
                """INSERT INTO sensor_logging_sensor
                    VALUES (%s, %s, CURRENT_DATE, CURRENT_TIME, DEFAULT);""",
                (sensor_id, sensor_data,))
        except:
            print("I can't INSERT into sensor_logging_sensor")
            return 'not OK'

        conn.commit()
        cur.close()
        conn.close()

        return 'OK'

    def read_continuously(self):

        usb = UsbReader(self.port, self.baudrate)
        try:
            while 1:
                try:
                    sensor_id, sensor_data = usb.read_value()
                    if sensor_id is not None and sensor_data is not None:
                        usb.write_to_db(sensor_id, sensor_data)
                except ValueError:
                    print("ValueError exception happened while reading...")
                    pass
                except TypeError:
                    print("TypeError exception happened while reading...")
                    pass      
        except KeyboardInterrupt:
            print("Program has stopped")
