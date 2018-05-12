import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 17  
Motor1B = 27   
Motor1E = 23   
Motor1F = 24   

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT) 
GPIO.setup(Motor1F,GPIO.OUT)

#forward

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(0.1)

GPIO.cleanup()


