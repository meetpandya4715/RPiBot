
import RPi.GPIO as GPIO
import time

duty = float(5)
pwm = None

def initpud():
    global duty
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 50)
    pwm.start(duty)


def pistolservoup(event):    
    global duty
    if(duty < 100):
        duty = duty + 0.1
        pwm.ChangeDutyCycle(duty)

def pistolservodown(event):
    global duty
    if(duty > 0):
        duty = duty - 0.1
        pwm.ChangeDutyCycle(duty)
    
