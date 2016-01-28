from iobeam import iobeam

import datetime
import time

###########################
# Template for a basic instrumentation app.
#
# This template outlines a script that periodically transmits device instrumentation
# data (e.g., temperature, humidity, gps, etc.) to iobeam.
#
# Instructions:
#
# 0. Add your project info below and name this device
#
# 1. Run with placeholder data from command line:
#     python instrumentation.py
#
# 2. Replace placeholder data with device specific code below in each of the 
#    template functions
#
# 3. Run again with your real data!
#
#
###########################


###########################
# Your project info
###########################
PROJECT_ID = # YOUR PROJECT ID HERE (int)
PROJECT_TOKEN = # YOUR PROJECT TOKEN HERE (String)
DEVICE_ID = # ID FOR THIS DEVICE (String)
DEVICE_NAME = # NAME FOR THIS DEVICE (String, can be the same as DEVICE_ID)

###########################
# Template functions
# NOTE: Fill your own code here
###########################
def get_temperature():
  return 72 # placeholder

def get_humidity():
  return 0.6 # placeholder

def get_gps():
  return (42.359155,-71.0952463) # placeholder

###########################
# Data collection / transmission
###########################
def main():
  # Build iobeam client
  builder = iobeam.ClientBuilder(PROJECT_ID, PROJECT_TOKEN).saveToDisk().registerOrSetId(DEVICE_ID, deviceName=DEVICE_NAME)
  client = builder.build()

  # Create data store with schema for transmitted data
  # Note: Update this schema with any new instrumentation data types
  measurements = client.createDataStore(["temperature", "humidity", "lat", "long"])

  # Loop
  while True:
    # Collect data
    now = int(time.time()*1000)
    temperature = get_temperature()
    humidity = get_humidity()
    gps_lat, gps_long = get_gps()

    # Add data points to data store
    measurements.add(now, {"temperature": temperature, "humidity": humidity, "lat": gps_lat, "long": gps_long})

    # Send data to iobeam
    client.send()

    # Print out data for debugging
    dt = datetime.datetime.fromtimestamp(now/1000.0)
    print('Sent: (Temperature: {:.2f}, Humidity: {:.2f}, (Lat, Long): ({:.6f}, {:.6f}) at {}'.format(temperature, humidity*100, gps_lat, gps_long, dt))

    # Sleep for a bit (30 sec)
    time.sleep(30)

if __name__ == "__main__":
    main()
