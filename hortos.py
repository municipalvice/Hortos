#!/usr/bin/env python3
import time, sched
from weather import get_weather

scheduler = sched.scheduler(time.time, time.sleep)

def schdule_reading(sc):
    weather = get_weather()
    humidity = weather['humidity']
    if (humidity < 55.0) {
        humidifier_on()
    } elif (humidity > 85.0) {
        humidifier_off()
    }
    scheduler.enter(6, 1, schdule_reading, (sc,))

try:
    scheduler.enter(6, 1, schdule_reading, (scheduler, ))
    scheduler.run()
except:
    print("Unable to record weather...")

if __name__ == '__main__':
    pass