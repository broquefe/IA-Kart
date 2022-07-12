import pigpio
import time

#Enable pigpio on command line prior to running code using --> sudo pigpiod
#Connect driver DIR to BCM 4
#Connect driver PUL to BCM 17
PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).

pi = pigpio.pi()

delay = 0.025

#pi.write(DIR, 0) # set local Pi's gpio BCM 4 low


durationFwd = 22 # This is the duration of the motor spinning. used for forward direction
durationBwd = 22 # This is the duration of the motor spinning. used for reverse direction
print('Duration Fwd set to ' + str(durationFwd))
print('Duration Bwd set to ' + str(durationBwd))

delay = 0.00009 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print('Speed set to ' + str(delay))
cycles = 1000 # This is the number of cycles to be run once program is started.
cyclecount = 0 # This is the iteration of cycles to be run once program is started.
print('number of Cycles to Run set to ' + str(cycles))

def forward():
    pi.write(ENA, 1)
   
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    pi.write(DIR, 0)
    
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        pi.write(PUL, 1)
        sleep(delay)
        pi.write(PUL, 0)
        sleep(delay)
    pi.write(ENA, 0)
    
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return


def reverse():
    pi.write(ENA, 1)
   
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    pi.write(DIR, 1)
    
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        pi.write(PUL, 1)
        sleep(delay)
        pi.write(PUL, 0)
        sleep(delay)
    pi.write(ENA, 0)
    
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return


while cyclecount < cycles:
    forward()
    
    reverse()
    #GPIO.output(DIR, GPIO.HIGH)
    #print('GPIO HIGH')
    #sleep(5)

    cyclecount = (cyclecount + 1)
    print('Number of cycles completed: ' + str(cyclecount))
    print('Number of cycles remaining: ' + str(cycles - cyclecount))
#
pi.stop()
print('Cycling Completed')