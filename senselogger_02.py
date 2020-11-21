from sense_hat import SenseHat
from datetime import datetime
from csv import writer

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())
    sense_data.append(datetime.now())
    
    return sense_data

#while True:
#    print(get_sense_data())

ftime = datetime.now()

timestamp = datetime.now()
delay = 1

with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','hum','press','datetime'])

    while True:
        data = get_sense_data()
        dt = data[-1] - timestamp
        if dt.seconds > delay:
            data_writer.writerow(data)
            timestamp = datetime.now()
        

