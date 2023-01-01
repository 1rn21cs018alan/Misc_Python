#drawing with python
import pyautogui
import time
import random
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
            pyautogui.moveTo(x,y)
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
            pyautogui.moveTo(x,y)
            return False
        else:
            return True
    else :
        return True
    


pyautogui.click(243,70)
pyautogui.click(243,70)
time.sleep(0.1)
pyautogui.click(150,200)

d=500
def draw(d):
    pyautogui.dragRel( d , 0 )
    while d>0:
        pyautogui.dragRel( 0 , d )
        pyautogui.dragRel( -d , 0 )
        pyautogui.dragRel( 0 , (5-d) )
        pyautogui.dragRel( (d-5) , 0)

        d-=10
    return


def draw2(d,b):
    pyautogui.dragRel( d , 0 )
    while d>0:
        pyautogui.dragRel( 0 , d )
        pyautogui.dragRel( -d , 0 )
        pyautogui.dragRel( 0 , (b-d) )
        pyautogui.dragRel( (d-b) , 0)

        d-=(2*b)
    return


def drawRan(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0
    a=p/4
    while d>0:
        pyautogui.dragRel( 0 , d )
        ra(a,d,4)
        pyautogui.dragRel( -d , 0 )
        ra(a,d,3)
        pyautogui.dragRel( 0 , (b-d) )
        ra(a,d,1)
        pyautogui.dragRel( (d-b) , 0)
        ra(a,d,2)
        d-=(2*b)
    return


def drawRand(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0.0
    a=p/4
    sq=True
    while d>0:
        pyautogui.dragRel( 0 , d )
        if sq:
            sq=ra2(a,d,4)
        pyautogui.dragRel( -d , 0 )
        if sq:
            sq=ra2((a*2),d,3)
        pyautogui.dragRel( 0 , (b-d) )
        if sq:
            sq=ra2((a*3),d,1)
        pyautogui.dragRel( (d-b) , 0)
        if sq:
            sq=ra2(p,d,2)
        d-=(2*b)
        sq=True
    return



def drawRandom(d,b,p):
    pyautogui.dragRel( d , 0 )
    a=0.0
    a=p/4
    sq=True
    sc=4
    while d>0:
        pyautogui.dragRel( 0 , d )
        sc-=1
        if sq and sc==0:
            sq=ra2(p,d,4)
            sc=4
        pyautogui.dragRel( -d , 0 )
        sc-=1
        if sq and sc==0:
            sq=ra2((p),d,3)
            sc=4
        pyautogui.dragRel( 0 , (b-d) )
        sc-=1
        if sq and sc==0:
            sq=ra2((p),d,1)
            sc=4
        pyautogui.dragRel( (d-b) , 0)
        sc-=1
        if sq and sc==0:
            sq=ra2(p,d,2)
            sc=4
        d-=(2*b)
        sq=True
    return



def loop(a,b):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
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
    pyautogui.moveTo(x,y)


    return

def randcircle2(d):
    xmin=10+d
    xmax=1560-d
    ymin=150+d
    ymax=800-d
    x=random.choice(range(xmin,xmax))
    y=random.choice(range(ymin,ymax))
    pyautogui.moveTo(x,y)
    
    return x,y

def circle1(radius):   ##2nd quadrant-->1st-->4th-->3rd ,aka clockwise from 9'o Clock
    randcircle(radius)
    ###2nd quadrant

    return

def circle2(radius):#the circle is drawn cloumn by cloumn
    
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    x,y=randcircle2(radius)
    
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            a=float(i*i)+(j*j)           #checking equation
            b=float(radius)
            if a>((b-0.5)*(b-0.5)) and a<((b+0.5)*(b+0.5)):
                pyautogui.click((x+i),(y+j))            
        
    return

def circlelistmode(radius):#conclusion: too slow
    
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    x,y=randcircle2(radius)
    clicklist=list()
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            a=float(i*i)+(j*j)           #checking equation
            b=float(radius)
            if a>((b-0.5)*(b-0.5)) and a<((b+0.5)*(b+0.5)):
                clicklist.append([(x+i),(y+j)])
    for each in clicklist:
        pyautogui.click(each[0],each[1])
        
    return
####

def loops(loops,size,density):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        
        draw2(size,density)
        loops-=1
        time.sleep(2)
    return

def RandLoop1(loops,size,density):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        draw2(size,density)
        ra(100,size,1)
        loops-=1
        time.sleep(3)
    return


def RandLoop2(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
    while loops>0:
        drawRan(300,5,0)
        ra(100,300,1)
        loops-=1
        
    return


def Ram(loops):
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
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
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
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
    pyautogui.click(243,70)
    pyautogui.click(243,70)
    time.sleep(0.1)
    pyautogui.click(150,200)
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

