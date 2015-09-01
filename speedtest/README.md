# Example: Speedtest

This is a basic example that shows how easy it is to collect and send multiple data points to **iobeam**.

Note: This uses the third-party [speedtest-cli](https://github.com/sivel/speedtest-cli) library.

## Getting Started 

1. If you haven't already: [register with iobeam](https://app.iobeam.com/signup), and create a new project

1. Grab your project's `ID` and `Project token` from the [Settings page](https://app.iobeam.com/)

1. In `speedtest.py`, replace the `PROJECT_ID` and `PROJECT_TOKEN` with the values for your project

1. Via your command-line, install [speedtest-cli](https://github.com/sivel/speedtest-cli): `pip install speedtest-cli`

1. Via your command-line, run the sample app: `python speedtest.py`

1. Look at your brand new data points via the [dashboard](https://app.iobeam.com/dashboard)

Note: The speedtest output results are also saved in a file (`speedtest.out`) in this same directory so you can easily look at the raw values. The values will look something like this (but hopefully with faster speeds!):

    Ping: 5.707 ms
    Download: 4.75 Mbyte/s
    Upload: 2.85 Mbyte/s

