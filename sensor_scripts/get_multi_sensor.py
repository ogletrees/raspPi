# 2023-09-17
# get data from 3 sensors

# libraries
import time
import csv
import board
import adafruit_ahtx0

import RPi.GPIO as GPIO
import os
import re
# from csv import writer
from datetime import datetime


# Initialize the AHT20 sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# get one-wire sensor data
# it is all under directories in /sys/bus/w1/devices/...
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# define function
def getTemps():
  allTemps = list()
  ow_basedir = "/sys/bus/w1/devices/"
  ow_devices = os.listdir(ow_basedir)
  ow_retemp = re.compile('t=(\d*)')
  for thistring in ow_devices:
    if(thistring.startswith("28")):
      ow_path = os.path.join(ow_basedir, thistring, "w1_slave")
      ow_devfile = open(ow_path, "r")
      ow_devtext = ow_devfile.readlines()
      ow_temp = ow_retemp.search(ow_devtext[1])
      allTemps.append(ow_temp.group(1))
  return(allTemps)
# allTemps should be data from all one-wire sensors connected

# ------------------------------------------------
# get values and print
# ------------------------------------------------
dt = datetime.now()
dt_string = dt.strftime("%Y%m%d_%H%M%S")


while True:
    allTemps = getTemps() # 1wire
    allTemps = [int(i) for i in allTemps]
    allTemps = [x//1000 for x in allTemps]
    
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    
    dtt = datetime.now()
    vals = dtt.strftime("%Y-%m-%d %H:%M:%S")
    allTemps.append(temperature)
    allTemps.append(humidity)
    allTemps.append(vals)
    #print(recs)
    # data_writer.writerow(allTemps)
    print(allTemps)
    

        
#     print(temperature, humidity)
#     # print(type(temperature))
#     allTemps.append(temperature)
#     print(allTemps)
    
    time.sleep(10)

