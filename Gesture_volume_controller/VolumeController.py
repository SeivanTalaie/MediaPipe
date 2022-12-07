import cv2 as cv
import mediapipe as mp
from mediapipe.python.solutions.hands import HandLandmark
import HandTrackingModule as htm
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)
cap =cv.VideoCapture(0)
cap.set(3,1500) # for resizing webcam window  ( width )
cap.set(4,1500) # for resizing webcam window  ( hight )

detector=htm.handDetector()


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange())
while True:
    _,frame =cap.read() 
    frame=detector.findHands(frame)
    # frame[50,70 , 100:150]=img
    list=detector.findposition(frame,handNo=0,draw=False) 
    if len(list)!=0:
        x1,y1= list[4][1] , list[4][2]
        x2,y2= list[8][1] , list[8][2]
        x3,y3= (x1+x2)//2,(y1+y2)//2
        

        cv.circle(frame,(x1,y1),10,blue,-1)
        cv.circle(frame,(x2,y2),10,blue,-1)
        cv.circle(frame,(x3,y3),10,blue,-1)

        cv.line(frame,(x1,y1),(x2,y2),blue,2)
        length=np.hypot(x2-x1,y2-y1)   # finding the lenght of a line 
        # print(int(lenght)) 10- 430
        if length<50:
            cv.circle(frame,(x3,y3),10,green,-1)
        if length>400:
            cv.circle(frame,(x3,y3),10,red,-1)

        vol=np.interp(length,[10,430],[-65.22,0])  #tabdi 1 mahdode be 1 mahdode dige
        volume.SetMasterVolumeLevel(vol, None)
  
    cv.imshow('hand tracking',frame)
    if cv.waitKey(1)==ord('s'):
        break
 



