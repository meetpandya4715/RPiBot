import RPi.GPIO as GPIO
from time import sleep
    
def riflereload():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    
    GPIO.setup(Motor1A,GPIO.OUT)

    #rifle reload

    print ("Rifle Reloaded")

    GPIO.output(Motor1A,GPIO.HIGH)

    sleep(2)

    GPIO.cleanup()

def rifleshoot():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    
    Motor1B = 6
    
    
    GPIO.setup(Motor1B,GPIO.OUT)
    

    #Rifle Shoot

    print ("Turning Motor Forward")

    
    GPIO.output(Motor1B,GPIO.HIGH)
    
    sleep(1)

    GPIO.cleanup()

def pistolreload():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1E = 13
    

    GPIO.setup(Motor1E,GPIO.OUT) 
    

    #Pistol Reload

    print ("Pistol Reloaded")

    GPIO.output(Motor1E,GPIO.LOW)
    
    sleep(2)

    GPIO.cleanup()


def pistolshoot():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1F = 19


    GPIO.setup(Motor1F,GPIO.OUT)


    #Pistol Shoot

    print ("Pistol Shoot")

    GPIO.output(Motor1F,GPIO.LOW)

    sleep(1)

    GPIO.cleanup()