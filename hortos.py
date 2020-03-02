#!/usr/bin/env python3

from record import record
from weather import get_weather

try:
    # Get weather reading
    weather = get_weather()
    # Record weather reading
    record(weather)    
except:
    print("Unable to record weather...")

if __name__ == '__main__':
    pass