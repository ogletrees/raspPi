import time
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT22(board.D4)



while True:
    t_c = dhtDevice.temperature
    hum = dhtDevice.humidity
    print('Temp: ' + str(t_c) + '; Hum: ' + str(hum))
    time.sleep(60)