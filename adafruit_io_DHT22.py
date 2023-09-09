# Adafruit_DHT is old library, py 2
import Adafruit_DHT
import time
from datetime import datetime
from csv import writer
from Adafruit_IO import Client
# import board
sensor = Adafruit_DHT.DHT22
pin = 11
aio = Client('sogletree', 'key')

dt = datetime.now()
dt_string = dt.strftime("%Y%m%d_%H%M")

with open('/home/pi/data/dataDHT_' + dt_string + '.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','humid','datetime'])

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        if humidity is not None and temperature is not None:
            temp_c = temperature
            temp_f = temperature * 9.0 / 5.0 + 32.0
            dt1 = datetime.now()
            sense_data = []
            sense_data.append(temp_c)
            # sense_data.append(temp_f)
            sense_data.append(humidity)
            sense_data.append(dt1.strftime("%Y-%m-%d %H:%M:%S.%f"))
            data_writer.writerow(sense_data)
            print(sense_data)
        else:
            dte = datetime.now()
            data_writer.writerow(['999.99','999.9',dte.strftime("%Y-%m-%d %H:%M:%S.%f")])
            print(['999.99','999.9',dte])
            
        humfeed = aio.feeds('humidity')
        aio.send_data(humfeed.key, humidity)        
        tempfeed = aio.feeds('temperature')
        aio.send_data(tempfeed.key, round(temp_f,2))    
        time.sleep(30)
