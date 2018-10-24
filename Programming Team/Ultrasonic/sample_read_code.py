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
    
left_front_dist = 0
right_front_dist = 0

front_dist = 0
back_dist = 0

left_back_dist = 0
right_back_front_dist = 0

previous = []
current = [left_front_dist, right_front_dist,

if (left_front_dist < 20 and front_dist < 5):
	#stop
	break