import cv2 as cv
import cvzone 
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


blue=(255,0,0)
red=(0,0,255)

cap= cv.VideoCapture(0)
# cap.set(3,1800)
# cap.set(4,1000)
detector=FaceMeshDetector(maxFaces=1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()


while True : 
    _,img=cap.read()
    ImgText=np.zeros_like(img)

    img,faces=detector.findFaceMesh(img,draw=False)

    if faces :
        face=faces[0]
        pointLeft=face[145]
        pointRight=face[374]
      

        w,_=detector.findDistance(pointLeft,pointRight)
        W=6.3
       
        f=590
        d=(W*f)/w
        # print(d)

        cvzone.putTextRect(img,f'Depth:{int(d)}cm',(face[10][0]-80,face[10][1]-50),scale=1.85)

        vol=np.interp(int(d),[20,73],[-65.22,0])  
        volume.SetMasterVolumeLevel(vol, None)       

    stacked=cvzone.stackImages([img,ImgText],2,1)
    cv.imshow("webcam",stacked)
    if cv.waitKey(1) == ord ("s") : 
        break
    