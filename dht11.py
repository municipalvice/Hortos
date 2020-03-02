#!/usr/bin/env python3

import adafruit_dht
import board
import time

pin = '18'
dht = adafruit_dht.DHT22(pin)

def get_reading() -> dict:
    """Returns the DHT22 reading: temperature in C and humidity as a percentage."""
    reading = {'temperature': None, 'humidity': None}
    print("Getting sensor reading...")

    while (reading['temperature'] is None or reading['humidity'] is None):
        try:
            time.sleep(2)
            reading['temperature'] = dht.temperature
            
            time.sleep(2)
            reading['humidity'] = dht.humidity

            print("Initial reading:", reading)
            return reading
        except RuntimeError as e:
            print("Reading from DHT failed", e.args)

if __name__ == "__main__":
    pass