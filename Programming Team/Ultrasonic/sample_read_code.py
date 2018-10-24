#/usr/bin/python

#Author Sahil Kapur

import datetime
import ultrasonic

def init():
    dm = sensor.initialize_sensor(trig, echo)
    return dm

def read_value(dm):
    dist = sensor.measure_distance(dm)
    return dist