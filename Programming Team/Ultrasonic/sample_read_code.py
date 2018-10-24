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
current = [left_front_dist, right_front_dist, front_dist, back_dist, left_back_dist, right_back_front_dist]
#0 is left front, 1 is right front, 2 is front, 3 is back, 4 is left back, 5 is right back
previous[0] = current; #0 is the most recent and 5 is the oldest data.
def storeNew():
	for x in xrange(5,1):
		previous[x] = previous[x-1];
		pass
	previous[0] = current;


if (left_front_dist < 20 and front_dist < 5):
	#stop
	break