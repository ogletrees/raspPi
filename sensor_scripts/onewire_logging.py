# 2023-09-09
# Python script for recording data from multiple sensors - one-wire
# to be run in Python 3 environment ideally

# libraries
import RPi.GPIO as GPIO
import os
import re
from csv import writer
from datetime import datetime
import time

# get one-wire sensor data
# it is all under directories in /sys/bus/w1/devices/...
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

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

dt = datetime.now()
dt_string = dt.strftime("%Y%m%d_%H%M")


# write data to csv
# open a new file names with current data-time
with open('data/data1w_' + dt_string + '.csv', 'w', newline = '') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','temp','datetime'])
  	# write to file, appending new data as it goes
    try:
      while True:
        allTemps = getTemps()
        #recs = []
        #ntemp = float(allTemps[0])/1000
        dtt = datetime.now()
        vals = dtt.strftime("%Y-%m-%d %H:%M:%S.%f") 
        #recs.append(ntemp)
        allTemps.append(vals)
        #print(recs)
        data_writer.writerow(allTemps)
        print(allTemps)
        time.sleep(5)
    
    except KeyboardInterrupt:
      print("Cleanup")
      GPIO.cleanup()
  