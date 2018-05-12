import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.OUT)

input_value = GPIO.input(7)
GPIO.output(8,True)
