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
current = [left_front_dist, right_front_dist, front_dist, back_dist, left_back_dist, right_back_dist]
#0 is left front, 1 is right front, 2 is front, 3 is back, 4 is left back, 5 is right back
action = [go_right_back,go_left_back,go_back,go_front,go_right_front,go_left_front]
previous[0] = current; #0 is the most recent and 5 is the oldest data.
def storeNew():
	for x in xrange(20,1):
		previous[x] = previous[x-1];
		pass
	previous[0] = current;


lowestbound = 3
largestbound = 517
for x in xrange(0,5):
	if current[x] == lowestbound - 1 and previous[1][x] == lowestbound:
		stop the car immediately
		pass

for x in xrange(3,5):
	if current[x] = lowestbound and previous[1][x] > lowestbound:
		stop doing anything, recalculate current path
		pass
	if current[x] = lowestbound and previous[1][x] <= lowestbound:
		pass
	

for x in xrange(0,5):
	if current[x] == 0:
		if previous[1][x] > 3 or largestbound:
			stop the car immediately #some thing unexpected happened
		pass
	pass

for x in xrange(0,5):
	if current[x] == lowestbound or current[x] <= lowestbound:
		do action[x]
	pass


#just a note, since we are storing the current and previous in a 2d array, we can use neural network to process them
