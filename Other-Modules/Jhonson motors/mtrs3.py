import RPi.GPIO as GPIO
from time import sleep

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

def forward(x):
    init()
    pwm=GPIO.setup(17, HIGH)
    pwm=GPIO.setup(22, HIGH)
    pwm=GPIO.setup(23, HIGH)
    pwm=GPIO.setup(24, HIGH)
    pwm.start(10)
    time.sleep(x)
    GPIO.cleanup()

def left(x):
    init()
    pwm=GPIO.setup(17, False)
    pwm=GPIO.setup(22, False)
    pwm=GPIO.setup(23, False)
    pwm=GPIO.setup(24, False)
    pwm.start(10)
    time.sleep(x)
    GPIO.cleanup()

def forward(x):
    init()
    pwm=GPIO.setup(17, True)
    pwm=GPIO.setup(22, True)
    pwm=GPIO.setup(23, False)
    pwm=GPIO.setup(24, False)
    pwm.start(10)
    time.sleep(x)
    GPIO.cleanup()

def right(x):
    init()
    pwm=GPIO.setup(17, True)
    pwm=GPIO.setup(22, True)
    pwm=GPIO.setup(23, True)
    pwm=GPIO.setup(24, True)
    pwm.start(10)
    time.sleep(x)
    GPIO.cleanup()

def reverse(x):
    init()
    pwm=GPIO.setup(17, True)
    pwm=GPIO.setup(22, True)
    pwm=GPIO.setup(23, True)
    pwm=GPIO.setup(24, True)
    pwm.start(10)
    time.sleep(x)
    GPIO.cleanup()


print ("forward")
forward(4)

print ("left")
left(4)
    
print ("forward")
forward(4)

print ("right")
right(4)

print ("reverse")
reverse(2)
