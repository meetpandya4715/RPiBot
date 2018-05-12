import RPi.GPIO as GPIO
from time import sleep


def m36dcm():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    
    GPIO.setup(Motor1A,GPIO.OUT)

    #36 DC MOTOR RUN

    print ("36 DC MOTOR ON")

    GPIO.output(Motor1A,GPIO.HIGH)

    sleep(0.4)

    GPIO.cleanup()


def m46dcm():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1B = 6

    GPIO.setup(Motor1B,GPIO.OUT)

    # 46 DC MOTOR ON

    print ("46 DC MOTOR ON")

    GPIO.output(Motor1B,GPIO.HIGH)
    
    sleep(0.4)

    GPIO.cleanup()