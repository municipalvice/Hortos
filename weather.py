#!/usr/bin/env python3 
from dht11 import get_reading

class Error(Exception):
    """Base exception class"""
    pass

class HumidityOutOfBounds(Error):
    """Raised when the humidity reading is not from 0 - 100 percent."""
    pass
class TemperatureOutOfBounds(Error):
    """Raised when the temperature reading is not from -40 to 80 Celcius."""
    pass

def get_weather() -> dict:
    try:
        # get weather (reading) from sensor
        weather = get_reading()
        
        # Check if reading is within specification: https://learn.adafruit.com/dht/overview
        # Good for 0-100% humidity readings with 2-5% accuracy
        if (weather['humidity'] < 0  or weather['humidity'] > 100 ):
            raise HumidityOutOfBounds
        # Good for -40 to 80°C temperature readings ±0.5°C accuracy
        elif (weather['temperature'] < -40 or weather['temperature'] > 80):
            raise TemperatureOutOfBounds
        else:
            # convert temperature to Farenheit
            weather['temperature'] = round(((weather['temperature'] * (9/5)) + 32), 1)
            
            return weather
    except HumidityOutOfBounds:
        print("The humidity reading is not from 0 - 100 percent.")
    except TemperatureOutOfBounds:
        print("The temperature reading is not from -40 to 80 Celcius.")
    # except:
    #    print("There was an issue reading from the sensor.")
if __name__ == "__main__":
    get_weather()