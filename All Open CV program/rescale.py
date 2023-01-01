import cv2 as cv


def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def scaling(scale,count):
    if(count%100<50):
        scale=scale*0.99
    else:
        scale=scale/0.99
    return scale
        

img=cv.imread('Capture.png')

#cv.imshow('Cat',img)

count =0
scale=1
speed=2
speed=(int)(input("Enter speed\n"))
timegap=(int)(20/speed)
capture = cv.VideoCapture("vid1.mp4")
while(True):

    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    count+=1
    if(count==7619):
        break;
    if(count%speed<3):
        if cv.waitKey(timegap+1) & 0xFF==ord('d'): 
            break;
capture.release()

cv.destroyAllWindows()

cv.waitKey(0)
capture = cv.VideoCapture("vid1.mp4")
scale=1
while(True):

    isTrue, frame=capture.read()
    cv.imshow('Video',rescale(frame,scale))
    scale=scaling(scale,count)
    count+=1
    if(count==7619):
        break;
    if(count%speed<3):
        if cv.waitKey(timegap) & 0xFF==ord('d'): 
            break;
capture.release()

cv.destroyAllWindows()

cv.waitKey(0)

