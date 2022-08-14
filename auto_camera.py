from datetime import datetime
from picamera import PiCamera
from time import sleep
import subprocess

camera = PiCamera()

# get date time for file name
# make file name
# take image
# save with file name
# sleep to make sure the image is saved
# try: rclone to move image to Drive, that will remove locally
# except: write msg to log file
# figure sleep time until next time point
# sleep

tp = [15, 30, 45, 60]

while True:
    now = datetime.now()
    fname1 = str(now.strftime("%Y_%m_%d-%H_%M_%S"))
    fname = str("image_" + fnn + ".jpg")
    # take image
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    sleep(15)
    # move to cloud
    try:
        subprocess.run(["rclone "])
    except:
        pass # just empty line, could also write to log
    
    # determine sleep time
    now2 = datetime.now()
    pmin = int(now2.strftime("%M"))
    dmins = tuple(q - pmin for q in tp)
    m = min(i for i in dmins if i > 0) * 60
    sleep(m)