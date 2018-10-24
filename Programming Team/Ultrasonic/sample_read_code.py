#/usr/bin/python

#Author Sahil Kapur

import datetime
import ultrasonic

def get_distance():
    dm = sensor.initialize_sensor()
    dist = sensor.measure_distance(dm)
    return dist