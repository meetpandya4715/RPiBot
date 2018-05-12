import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor1A = 23  #RIFLE RELOAD
Motor1B = 24  #RIFLE Shoot
Motor1E = 17   #PISTOL RELOAD
Motor1F = 27   #PISTOL SHOOT

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT) 
GPIO.setup(Motor1F,GPIO.OUT)

#RIFLE RELOAD

GPIO.output(Motor1A,GPIO.HIGH)

sleep(2)

#Delay

GPIO.output(Motor1A,GPIO.LOW)

sleep(2)

#RIFLE SHOOTING

GPIO.output(Motor1B,GPIO.HIGH)

sleep(5)

#Delay

GPIO.output(Motor1B,GPIO.LOW)

sleep(2)

#PISTOL RELOAD

GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)

#Delay

GPIO.output(Motor1E,GPIO.LOW)

sleep(2)

#PISTOL SHOOTING

GPIO.output(Motor1F,GPIO.HIGH)

sleep(2)

#Delay

GPIO.output(Motor1F,GPIO.LOW)

sleep(2)

GPIO.cleanup()
