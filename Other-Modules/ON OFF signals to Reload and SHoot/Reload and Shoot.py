import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 12
Motor1B = 19
Motor1E = 13
Motor1F = 6


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT) 
GPIO.setup(Motor1F,GPIO.OUT)

print ("Rifle Reload")

GPIO.output(Motor1A,GPIO.HIGH)
#GPIO.output(Motor1B,GPIO.HIGH)
#GPIO.output(Motor1E,GPIO.HIGH)
#GPIO.output(Motor1F,GPIO.LOW)

sleep(2)


#Delay

GPIO.output(Motor1A,GPIO.LOW)

sleep(2)

#Rifle Shoot

GPIO.output(Motor1B,GPIO.HIGH)

sleep(2)

#Delay

GPIO.output(Motor1B,GPIO.LOW)

sleep(2)


#Pistol Reload

GPIO.output(Motor1E,GPIO.HIGH)

sleep(1)

#Delay

GPIO.output(Motor1E,GPIO.LOW)

sleep(2)

#Pistol Shoot

GPIO.output(Motor1F,GPIO.HIGH)

sleep(1)


#Delay

GPIO.output(Motor1F,GPIO.LOW)

sleep(2)


GPIO.cleanup()
