from iobeam import iobeam

import datetime
import subprocess
import time

# Your project info
PROJECT_ID = # YOUR PROJECT ID HERE (int)
PROJECT_TOKEN = # YOUR PROJECT TOKEN HERE (String)

# Build iobeam client
# Note: In this example, we are choosing to register this device as a new device, 
# and save the device_id to disk (saved in the same directory)
builder = iobeam.ClientBuilder(PROJECT_ID, PROJECT_TOKEN).saveToDisk().registerDevice()
client = builder.build()

while True:
  # Get speedtest info
  # Note: You'll need to install speedtest-cli first (i.e., "pip install speedtest-cli")
  subprocess.call("speedtest-cli --bytes --simple > speedtest.out", shell=True)

  download = float(subprocess.check_output("awk '/Download: /{print $2;}' speedtest.out", shell=True)[0:-1])
  upload = float(subprocess.check_output("awk '/Upload: /{print $2;}' speedtest.out", shell=True)[0:-1])
  ping = float(subprocess.check_output("awk '/Ping: /{print $2;}' speedtest.out", shell=True)[0:-1])

  # Create new datapoints and send to iobeam
  now = int(time.time()*1000)
  d = iobeam.DataPoint(download, timestamp=now)
  u = iobeam.DataPoint(upload, timestamp=now)
  p = iobeam.DataPoint(ping, timestamp=now)

  # Look ma! I can send multiple data points at the same time!
  client.addDataPoint("download", d)
  client.addDataPoint("upload", u)
  client.addDataPoint("ping", p)
  client.send()

  dt = datetime.datetime.fromtimestamp(now/1000.0)
  print 'Sent: (Download: %.2f Mbyte/s, Upload: %.2f Mbyte/s, Ping: %.3f ms) at %s' % (download, upload, ping, dt)

  # Sleep for a bit (5 secs)
  time.sleep(5)
