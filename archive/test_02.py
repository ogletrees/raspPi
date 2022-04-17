import Adafruit_DHT
import time
from datetime import datetime
from csv import writer
sensor = Adafruit_DHT.DHT22
pin = 4
# humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#while True:
#    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#    
#    if humidity is not None and temperature is not None:
#        temp_f = temperature * 9.0 / 5.0 + 32.0
#        dt = datetime.now()
#        print ('Temp={0:0.2f}F Humdity={1:0.1f}% Time:{2}'.format(temp_f, humidity, dt))
#    else:
#        print('Failed')
#    time.sleep(20)

dt = datetime.now()
dt_string = dt.strftime("%Y%m%d_%H%M")

with open('data_' + dt_string + '.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','hum','datetime'])

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        if humidity is not None and temperature is not None:
            temp_f = temperature * 9.0 / 5.0 + 32.0
            dt1 = datetime.now()
            sense_data = []
            sense_data.append(temp_f)
            sense_data.append(humidity)
            sense_data.append(dt1.strftime("%Y-%m-%d %H:%M:%S.%f"))
            data_writer.writerow(sense_data)
            print(sense_data)
        else:
            dte = datetime.now()
            data_writer.writerow(['999.99','999.9',dte.strftime("%Y-%m-%d %H:%M:%S.%f")])
            print(['999.99','999.9',dte])
        time.sleep(20)
