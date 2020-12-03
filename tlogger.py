import RPi.GPIO as GPIO
import os
import re
import datetime

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

def getTemps():
  allTemps = list()
  ow_basedir = "/sys/bus/w1/devices/"
  ow_devices = os.listdir(ow_basedir)
  ow_retemp = re.compile('t=(\d*)')
  for thistring in ow_devices:
    if(thistring.startswith("28")):
      ow_path = os.path.join(ow_basedir, thistring. "w1_slave")
      ow_devfile = open(ow_path, "r")
      ow_devtext = ow_devfile.readlines()
      ow_temp = ow_retemp.search(ow_devtext[1])
      allTemps.append(ow_temp.group(1))
   return(allTemps)
  
try:
  while True:
    allTemps = getTemps()
    ntemp = float(allTemps[0]/1000)
    dt = datetime.now()
    print(ntemp.append(dt))

except KeyboardInterrupt:
  print("Cleanup")
  GPIO.cleanup()
  
