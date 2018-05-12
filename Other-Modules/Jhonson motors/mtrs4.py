import RPi.GPIO as GPIO
from time import sleep

def botmovebackward():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 27
    Motor1B = 17
    Motor1E = 23
    Motor1F = 24


    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT) 
    GPIO.setup(Motor1F,GPIO.OUT)


    #Turning Backwards

    print ("Turning Motor Backwards")

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1F,GPIO.HIGH)

    sleep(3)

    GPIO.cleanup()
