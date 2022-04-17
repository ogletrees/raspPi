from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    sense_data.append(datetime.now())
    
    return sense_data


print(get_sense_data())
