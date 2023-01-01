#drawing with python
import pyautogui
import time
import random
import mouse
# open paint and put it in the left , also move all the python window to the right
mouse.move(243,70,absolute=True)
mouse.click("left")
mouse.move(243,200,absolute=True)
mouse.click("left")
time.sleep(1)
def xy3dplane():
    a=150
    b=30
    mouse.drag(0,0,0,a,absolute=False,duration=0.1)
    mouse.drag(0,0,b,-b,absolute=False,duration=0.1)
    mouse.drag(0,0,0,-a,absolute=False,duration=0.1)
    mouse.drag(0,0,-b,b,absolute=False,duration=0.1)
    mouse.drag(0,0,0,(2*a),absolute=False,duration=0.1)
    mouse.drag(0,0,b,-b,absolute=False,duration=0.1)
    mouse.drag(0,0,0,(b-a),absolute=False,duration=0.1)
    time.sleep(0.2)
    mouse.move(0,-b,absolute=False,duration=0.1)
    mouse.drag(0,0,a,0,absolute=False,duration=0.1)
    mouse.drag(0,0,-b,b,absolute=False,duration=0.1)
    mouse.drag(0,0,((-2)*a),0,absolute=False,duration=0.1)
    mouse.drag(0,0,b,-b,absolute=False,duration=0.1)
    mouse.drag(0,0,(a-b),0,absolute=False,duration=0.1)


def vp():
    mouse.drag(0,0,0,-100,absolute=False,duration=0.1)
    mouse.drag(0,0,-80,20,absolute=False,duration=0.1)
    mouse.drag(0,0,0,100,absolute=False,duration=0.1)
    mouse.drag(0,0,80,-20,absolute=False,duration=0.1)

def pp():
    mouse.drag(0,0,0,-100,absolute=False,duration=0.1)
    mouse.drag(0,0,80,20,absolute=False,duration=0.1)
    mouse.drag(0,0,0,100,absolute=False,duration=0.1)
    mouse.drag(0,0,-80,-20,absolute=False,duration=0.1)

def hp():
    mouse.drag(0,0,80,20,absolute=False,duration=0.1)
    mouse.drag(0,0,-80,20,absolute=False,duration=0.1)
    mouse.drag(0,0,-80,-20,absolute=False,duration=0.1)
    mouse.drag(0,0,80,-20,absolute=False,duration=0.1)

def closeplane():
    vp()
    hp()
    pp()

def farplane():
    mouse.move(-40,-40,absolute=False,duration=0.2)
    vp()
    mouse.move(80,0,absolute=False,duration=0.2)
    pp()
    mouse.move(-40,80,absolute=False,duration=0.2)
    hp()
    mouse.move(0,-40,absolute=False,duration=0.2)
    mouse.click('left')
print("xy3dplane()\nvp()\npp()\nhp()\ncloseplane()\nfarplane()")

