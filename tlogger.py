import RPi.GPIO as GPIO
import os
import re
from datetime import datetime

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

dt = datetime.now()
dt_string = dt.strftime("%Y%m%d_%H%M")

with open('data_' + dt_string + '.csv', 'w', newline='') as f:
    data_writer = writer(f)
    data_writer.writerow(['temp','datetime'])
  
try:
  while True:
    allTemps = getTemps()
    ntemp = float(allTemps[0]/1000)
    dtt = datetime.now()
    vals = str(ntemp) + ', ' + dt.strftime("%Y-%m-%d %H:%M:%S.%f")
    data_writer.writerow(vals)
    print(vals)

except KeyboardInterrupt:
  print("Cleanup")
  GPIO.cleanup()
  
