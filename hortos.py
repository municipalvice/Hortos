#!/usr/bin/env python3
import dht11
import json
import sys

# const { spawn } = require('child_process')

# has to be able to call python from node and accept a JSON object/string
# - Call the above every 60 seconds or so to get weather reading often
#  Then, with that reading create a function that keeps the humidity w/in 50-80%

try:
    # returns dict with {'temperature': 0.0, 'humidity': 0.0}
    weather_reading = dht11.get_reading() 
    
    # convert temp from C to F
    weather_reading['temperature'] = (weather_reading['temperature'] * (9/5)) + 32
    
    # converts to JSON string (as below)
    json_reading = json.dumps(weather_reading)
    
    print("Returning JSONified weather reading...", json_reading)
    sys.stdout.flush()
    return json_reading
except:
    print("Unable to record weather...")

if __name__ == '__main__':
    pass