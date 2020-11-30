from gpiozero import LED, Button
from signal import pause

mySwitch = Button(2)
myLED = LED(26) #gpio BCM

myLED.blink()

pause()