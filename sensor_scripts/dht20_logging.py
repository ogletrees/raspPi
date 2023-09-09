# 2023-09-09
# script for logging data from DHT20 sensor
# may need this beforehand - sudo pip3 install adafruit-circuitpython-ahtx0

import time
import csv
import board
import adafruit_ahtx0

# Initialize the AHT20 sensor
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# File path for the CSV file
# csv_file = "./data/data_dht20.csv"

# Function to log temperature and humidity data to a CSV file
#def log_data_to_csv(temperature, humidity):
#    with open(csv_file, mode='a') as file:
#        writer = csv.writer(file)
#        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity])

# Main loop
while True:
    try:
        temperature = sensor.temperature
        humidity = sensor.relative_humidity

        # Log the data to the CSV file
        #log_data_to_csv(temperature, humidity)
        print(temperature, humidity)

        # Wait for 5 minutes before reading data again
        time.sleep(10)
    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
    except Exception as e:
        print(f"Error: {e}")
        # Continue on error

print("Data logging stopped.")
