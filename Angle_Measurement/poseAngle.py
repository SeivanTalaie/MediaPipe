import cv2 as cv
import numpy as np
import PoseDetectionModule as pdm 
import time


cap=cv.VideoCapture(0)
# cap.set(3,1500)
# cap.set(4,1500)
detector=pdm.PoseDetector()

count=0
dir=0

ptime=0
while True:
    _,frame=cap.read()
    resized=cv.resize(frame,(1600,1000))

    frame=detector.findPose(resized)
    list=detector.findposition(resized)
    angle=detector.findAngle(frame,12,14,16,draw=True)
    
    cv.putText(resized,f'angle={str(int(angle))}',(100,100),cv.FONT_HERSHEY_COMPLEX,2,(255,255,100),2)
    percentage=np.interp(angle,(95,155),(100,0))
    cv.putText(resized,f'percentage={str(int(percentage))}',(100,200),cv.FONT_HERSHEY_COMPLEX,2,(255,255,100),2)

    bar=np.interp(angle,(92,162),(200,800))
    color=(200,0,0)
    if dir == 0 :
        
        color=(0,0,200)
        if percentage == 100:
            count+=0.5
            dir = 1
    
    color=(200,0,0)
    
    if dir == 1:
        
        color=(0,200,0)
        if percentage == 0 :
            count+=0.5 
            dir=0
    cv.putText(resized,f'num= {str(int(count))}',(100,400),cv.FONT_HERSHEY_COMPLEX,2,(255,255,100),2)

    cv.rectangle(resized,(1350,200),(1450,800),color,2)
    cv.rectangle(resized,(1350,int(bar)),(1450,800),color,-1)
    cv.putText(resized,f'{str(int(percentage))}%',(1350,150),cv.FONT_HERSHEY_COMPLEX,2,(255,255,100),2)

    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(resized,f'FPS= {str(int(fps))}',(100,300),cv.FONT_HERSHEY_COMPLEX,2,(255,255,100),2)


    cv.imshow('webcam',frame)
    if cv.waitKey(1)==ord('s'):
        break
