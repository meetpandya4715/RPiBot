import RPi.GPIO as GPIO
from time import sleep


def botmoverear():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    Motor1B = 6
    Motor1E = 13
    Motor1F = 19

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor1F, GPIO.OUT)

    # Turning Backwards

    print("Turning Motor Backwards")

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor1F, GPIO.HIGH)

    sleep(0.04)

    GPIO.cleanup()


def botmovefront():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    Motor1B = 6
    Motor1E = 13
    Motor1F = 19

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor1F, GPIO.OUT)

    # Turning Forward

    print("Turning Motor Forward")

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor1F, GPIO.LOW)

    sleep(0.04)

    GPIO.cleanup()


def botmoveleft():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    Motor1B = 6
    Motor1E = 13
    Motor1F = 19

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor1F, GPIO.OUT)

    # Turning Left

    print("Turning Motor Left")

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor1F, GPIO.HIGH)

    sleep(0.04)

    GPIO.cleanup()


def botmoveright():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    Motor1A = 5
    Motor1B = 6
    Motor1E = 13
    Motor1F = 19

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor1F, GPIO.OUT)

    # Turning Right

    print("Turning Motor Right")

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor1F, GPIO.LOW)

    sleep(0.04)

    GPIO.cleanup()
