#drawing with python
import pyautogui
import time
import random
import mouse
# open paint and put it in the left , also move all the python window to the right
def ra(p,d,border):
    a=random.choice(range(0,10000))
    if a<(p*100):
        xmin=10+d
        xmax=1560-d
        ymin=150+d
        ymax=800-d
        if border==1: #starts at upper left 
            xmin=10
            ymin=150
        elif border==2: #starts at upper right 
            xmax=1560
            ymin=150
        elif border==3: #starts at lower left
            xmin=10
            ymax=800
        elif border==4: #starts at lower right
            xmax=1560
            ymax=800
        if xmin<xmax and ymin<ymax:
            x=random.choice(range(xmin,xmax))
            y=random.choice(range(ymin,ymax))
            mouse.move(x,y,absolute=True,duration=0.05)
            mouse.click("left")
    return


    
def ra2(p,d,border):
    a=random.choice(range(0,10000))
    if a<(p*100):
        xmin=10+d
        xmax=1560-d
        ymin=150+d
        ymax=800-d
        if border==1: #starts at upper left 
            xmin=10
            ymin=150
        elif border==2: #starts at upper right 
            xmax=1560
            ymin=150
        elif border==3: #starts at lower left
            xmin=10
            ymax=800
        elif border==4: #starts at lower right
            xmax=1560
            ymax=800
        if xmin<xmax and ymin<ymax:
            x=random.choice(range(xmin,xmax))
            y=random.choice(range(ymin,ymax))
            mouse.move(x,y,absolute=True,duration=0.05)
            mouse.click("left")
            return False
        else:
            return True
    else :
        return True
    


mouse.move(243,70,absolute=True)
mouse.click("left")
mouse.move(243,70,absolute=True)
mouse.click("left")
time.sleep(0.1)
mouse.move(150,200,absolute=True)
mouse.click("left")

d=500




def loop(a,b):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    while a>0:
        draw(b)
        a-=1
        time.sleep(2)
    return


####


def randcircle1(d):
    xmin=10+d
    xmax=1560-d
    ymin=150+d
    ymax=800-d
    x=random.choice(range(xmin,xmax))
    y=random.choice(range(ymin,ymax))
    mouse.move(x,y,absolute=True,duration=0.05)
    mouse.click("left")


    return

def randcircle2(d):
    xmin=10+d
    xmax=1560-d
    ymin=150+d
    ymax=800-d
    x=random.choice(range(xmin,xmax))
    y=random.choice(range(ymin,ymax))
    mouse.move(x,y,absolute=True,duration=0.05)
    mouse.click("left")
    
    return x,y

def circle1(radius):   ##2nd quadrant-->1st-->4th-->3rd ,aka clockwise from 9'o Clock
    randcircle1(radius)
    ###2nd quadrant

    return

def circle2(radius):#the circle is drawn cloumn by cloumn
    
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    x,y=randcircle2(radius)
    
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            a=float(i*i)+(j*j)           #checking equation
            b=float(radius)
            if a>((b-0.5)*(b-0.5)) and a<((b+0.5)*(b+0.5)):
                mouse.move((x+i),(y+j),absolute=True)
                mouse.click("left")
    
    return

def clm(radius):#conclusion: makes a filled circle since cursor moves up and down during drawing
    
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    x,y=randcircle2(radius)
    clicklist=list()
    tx=0
    ty=0
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            a=float(i*i)+(j*j)           #checking equation
            b=float(radius)
            if a>((b-0.5)*(b-0.5)) and a<((b+0.5)*(b+0.5)):
                clicklist.append([(x+i),(y+j)])
    tx=clicklist[0][0]
    ty=clicklist[0][1]            
    for each in clicklist:
        mouse.drag(tx,ty,each[0],each[1],absolute=True)
        tx=each[0]
        ty=each[1]
        
    return


def cl(n):
    for i in range(n):
        r=random.choice(range(10,300))
        circle2(r)
        time.sleep(2)
####

def loops(loops,size,density):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    while loops>0:
        
        draw2(size,density)
        loops-=1
        time.sleep(2)
    return

def RandLoop1(loops,size,density):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    while loops>0:
        draw2(size,density)
        ra(100,size,1)
        loops-=1
        time.sleep(3)
    return


def RandLoop2(loops):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    while loops>0:
        drawRan(300,5,0)
        ra(100,300,1)
        loops-=1
        
    return


def Ram(loops):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(4,25))
        ra(100,size,1)
        drawRan(size,density,p)
        loops-=1
        time.sleep(3)
    return

def Ram2(loops):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(4,25))
        ra(100,size,1)
        drawRandom(size,density,p)
        ra(100,size,1)
        draw2(size,density)
        loops-=1
        time.sleep(3)
    return

def Ram3(loops):
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    mouse.move(243,70,absolute=True)
    mouse.click("left")
    
    time.sleep(0.1)
    mouse.move(150,200,absolute=True)
    mouse.click("left")
    size,density,p=0,0,0
    while loops>0:
        size=random.choice(range(50,400))
        density=random.choice([3,4,5,6,7,8])
        p=random.choice(range(0,20))
        ra(100,size,1)
        drawRandom(size,density,p)
        loops-=1
        time.sleep(3)
    return
    
print(d)

