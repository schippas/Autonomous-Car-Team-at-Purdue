# https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

class DistanceMeasurer:
    
    def __init__(self, trig_pin, echo_pin, settle_time=1, range_min=2, range_max=500, mode=GPIO.BCM):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.settle_time = settle_time
        self.range_min = range_min
        self.range_max = range_max
        
        GPIO.setmode(mode)                          #Set GPIO pin numbering 
        GPIO.setup(trig_pin, GPIO.OUT)                  #Set pin as GPIO out
        GPIO.setup(echo_pin, GPIO.IN)                   #Set pin as GPIO in

    # This may not be a good idea as the object could go out of scope while the rest of the calling program
    # is still using GPIO port. Better handled by the calling program
    def __del__(self):
        GPIO.cleanup()

    def get_dist(self):
        GPIO.output(self.trig_pin, False)               #Set trig_pin as LOW
        #print "Waiting For Sensor To Settle"
        time.sleep(self.settle_time)                    #Delay of 2 seconds

        GPIO.output(self.trig_pin, True)                #Set trig_pin as HIGH
        time.sleep(0.00001)                             #Delay of 0.00001 seconds
        GPIO.output(self.trig_pin, False)               #Set trig_pin as LOW

        while GPIO.input(self.echo_pin)==0:             #Check whether the echo_pin is LOW
            pulse_start = time.time()                   #Saves the last known time of LOW pulse

        while GPIO.input(self.echo_pin)==1:             #Check whether the echo_pin is HIGH
            pulse_end = time.time()                     #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start        #Get pulse duration to a variable

        distance = pulse_duration * 17150               #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)                   #Round to two decimal points

        if distance > self.range_min and distance < self.range_max:      #Check whether the distance is within range
            #print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
            return distance
        else:
            raise RuntimeError ("Out Of Range %f" % distance)                   #display out of range

##############################################################################################################

def initialize_sensor():
    GPIO.setmode(GPIO.BCM)
    trig_pin = 23                                       
    echo_pin = 25                                       
    dm = DistanceMeasurer(trig_pin, echo_pin)
    
def measure_distance(dm):
    dist = None
    try:
        dist = dm.get_dist()
        print 'Distance is %f' % dist
    except RuntimeError, e:
        print 'ERR Distance is %s' % e
    return dist

def cleanup():
    GPIO.cleanup()