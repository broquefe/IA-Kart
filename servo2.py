import time
import pigpio

pi = pigpio.pi() # Connect to local Pi.

# AIY will say the string printed here
print("standing")

pi.set_servo_pulsewidth(26, 700)
# Sleeps are required so we don't pull too much current at once
time.sleep(1)
pi.set_servo_pulsewidth(18, 1500)
a = pi.get_pwm_dutycycle(18)
print(a)
time.sleep(1)
pi.set_servo_pulsewidth(18, 2200)
b = pi.get_pwm_dutycycle(18)
print(b)
time.sleep(1)
pi.set_servo_pulsewidth(18, 800)
c = pi.get_pwm_dutycycle(18)
print(c)
time.sleep(1)

pi.stop()