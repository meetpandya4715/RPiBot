from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 50)
pwm.start(7.5)

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=30,
              orient=VERTICAL, command=self.update)
        scale.grid(row=2)

    def update(self, angle):
        duty = float(angle) / 10.0 + 5.5
        pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x200+0+0")
root.mainloop()
