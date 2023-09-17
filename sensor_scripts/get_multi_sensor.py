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
    #recs = []
    #ntemp = float(allTemps[0])/1000
    dtt = datetime.now()
    vals = dtt.strftime("%Y-%m-%d %H:%M:%S.%f") 
    #recs.append(ntemp)
    allTemps.append(vals)
    #print(recs)
    data_writer.writerow(allTemps)
    print(allTemps)
    
    temperature = sensor.temperature
    humidity = sensor.relative_humidity
        
    print(temperature, humidity)
    time.sleep(5)

