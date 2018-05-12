from Tkinter import *

# Importing files for botmovement
import mtrs

# Importing files for botmovement
import m3646radcm

# Importing files for Reload and Shoot
import ras

# Importing Files for Pistol Servo Movement
import plr
import pud

# Importing Files for Rifle Servo Movement
import rlr
import rud

# Importing Files for Camera Servo Movement
import cslr
import csud

plr.initplr()
pud.initpud()

rlr.initrlr()
rud.initrud()

cslr.initcslr()
csud.initcsud()


# Bot Movement

def keypressed(event):
    keycode = event.keysym
    if keycode == "Left":
        print("Bot Movement Left")
        mtrs.botmoveleft()
    elif keycode == "Right":
        print("Bot Movement Right")
        mtrs.botmoveright()
    elif keycode == "Up":
        print("Bot Movement Front")
        mtrs.botmovefront()
    elif keycode == "Down":
        print("Bot Movement Rear")
        mtrs.botmoverear()

    # Rifle and Pistol Reload and Shoot

    elif keycode == "m":
        print("Rifle Reload")
        ras.riflereload()
    elif keycode == "comma":
        print("Rifle Shoot")
        ras.rifleshoot()
    elif keycode == "period":
        print("Pistol Reload")
        ras.pistolreload()
    elif keycode == "slash":
        print("Pistol Shoot")
        ras.pistolshoot()

    # 3.6 RA DC motor

    elif keycode == "bracketleft":
        print("36 DC Motor Run")
        m3646radcm.m36dcm()
    # elif keycode == "bracketright":
    # print("DC Motor M1 OFF")

    # 4.6 RA DC motor

    elif keycode == "semicolon":
        print("46 DC Motor Run")
        m3646radcm.m46dcm()
    # elif keycode == "apostrophe":
    # print("DC Motor M2 OFF")

    # Camera Servos

    elif keycode == "h":
        cslr.camservoleft(event)
        print("Camera Servo Left")
    elif keycode == "j":
        cslr.camservoright(event)
        print("Camera Servo Right")
    elif keycode == "k":
        csud.camservoup(event)
        print("camera Servo Up")
    elif keycode == "l":
        csud.camservodown(event)
        print("Camera Servo Down")

    # Pistol Servos

    elif keycode == "u":
        plr.pistolservoleft(event)
        print("Pistol Servo Left")
    elif keycode == "U":
        plr.pistolservoright(event)
        print("Pistol Servo Right")
    elif keycode == "i":
        pud.pistolservoup(event)
        print("Pistol Servo Up")
    elif keycode == "I":
        pud.pistolservodown(event)
        print("Pistol servo Down")

    # Rifle Servos

    elif keycode == "o":
        rlr.rifleservoright(event)
        print("Rifle Servo Left")
    elif keycode == "O":
        rlr.rifleservoleft(event)
        print("Rifle Servo Right")
    elif keycode == "p":
        rud.rifleservoup(event)
        print("Rifle Servo Up")
    elif keycode == "P":
        rud.rifleservodown(event)
        print("Rifle Servo Down")

    # Robotic Arm 1

    elif keycode == "1":
        print("RA1 servo1 front")
    elif keycode == "2":
        print("RA1 servo2 front")
    elif keycode == "3":
        print("RA1 servo3 front")
    elif keycode == "4":
        print("RA1 servo4 front")
    elif keycode == "5":
        print("RA1 servo5 front")
    elif keycode == "6":
        print("RA1 servo6 front")
    elif keycode == "exclam":
        print("RA1 servo1 rear")
    elif keycode == "at":
        print("RA1 servo2 rear")
    elif keycode == "numbersign":
        print("RA1 servo3 rear")
    elif keycode == "dollar":
        print("RA1 servo4 rear")
    elif keycode == "percent":
        print("RA1 servo5 rear")
    elif keycode == "asciicircum":
        print("RA1 servo6 rear")

    # Robotic Arm 2

    elif keycode == "q":
        print("RA2 servo1 front")
    elif keycode == "w":
        print("RA2 servo2 front")
    elif keycode == "e":
        print("RA2 servo3 front")
    elif keycode == "r":
        print("RA2 servo4 front")
    elif keycode == "t":
        print("RA2 servo5 front")
    elif keycode == "y":
        print("RA2 servo6 front")
    elif keycode == "Q":
        print("RA2 servo1 rear")
    elif keycode == "W":
        print("RA2 servo2 rear")
    elif keycode == "E":
        print("RA2 servo3 rear")
    elif keycode == "R":
        print("RA2 servo4 rear")
    elif keycode == "T":
        print("RA2 servo5 rear")
    elif keycode == "Y":
        print("RA2 servo6 rear")

    # Robotic Arm 3

    elif keycode == "a":
        print("RA3 servo1 front")
    elif keycode == "s":
        print("RA3 servo2 front")
    elif keycode == "d":
        print("RA3 servo3 front")
    elif keycode == "f":
        print("RA3 servo4 front")
    elif keycode == "g":
        print("RA3 servo5 front")
    elif keycode == "A":
        print("RA3 servo1 rear")
    elif keycode == "S":
        print("RA3 servo2 rear")
    elif keycode == "D":
        print("RA3 servo3 rear")
    elif keycode == "F":
        print("RA3 servo4 rear")
    elif keycode == "G":
        print("RA3 servo5 rear")

    # Robotic Arm 4

    elif keycode == "z":
        print("RA4 servo1 front")
    elif keycode == "x":
        print("RA4 servo2 front")
    elif keycode == "c":
        print("RA4 servo3 front")
    elif keycode == "v":
        print("RA4 servo4 front")
    elif keycode == "b":
        print("RA4 servo5 front")
    elif keycode == "Z":
        print("RA4 servo1 rear")
    elif keycode == "X":
        print("RA4 servo2 rear")
    elif keycode == "C":
        print("RA4 servo3 rear")
    elif keycode == "V":
        print("RA4 servo4 rear")
    elif keycode == "B":
        print("RA4 servo5 rear")

    # Robotic Arm 5

    elif keycode == "7":
        print("RA5 servo1 front")
    elif keycode == "8":
        print("RA5 servo2 front")
    elif keycode == "9":
        print("RA5 servo3 front")
    elif keycode == "0":
        print("RA5 servo4 front")
    elif keycode == "minus":
        print("RA5 servo5 front")
    elif keycode == "ampersand":
        print("RA5 servo1 rear")
    elif keycode == "asterisk":
        print("RA5 servo2 rear")
    elif keycode == "parenleft":
        print("RA5 servo3 rear")
    elif keycode == "parenright":
        print("RA5 servo4 rear")
    elif keycode == "underscore":
        print("RA5 servo5 rear")


root = Tk()

root.geometry("600x300")
root.title("Remote Control")

root.bind("<Key>", keypressed)

root.mainloop()
