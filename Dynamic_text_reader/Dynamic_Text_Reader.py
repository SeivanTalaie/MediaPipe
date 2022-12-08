import cv2 as cv
import cvzone 
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np 
cv.__version__

blue=(255,0,0)
red=(0,0,255)

cap= cv.VideoCapture(0)
# cap.set(3,400)
# cap.set(4,400)

detector=FaceMeshDetector(maxFaces=1)

text=['Hello','My name is:','Seivan Talaie','I hope You doing Well', 'And here','I will do an AI projects']

while True : 
    _,img=cap.read()
    img=resized=cv.resize(img,(700,600))

    ImgText=np.zeros_like(img)

    img,faces=detector.findFaceMesh(img,draw=False)
    # print(faces)

    if faces :
        face=faces[0]
        # print(face)
        pointLeft=face[145]
        pointRight=face[374]
      

        w,_=detector.findDistance(pointLeft,pointRight)
        W=6.3
       
        f=590
        d=(W*f)/w
        # print(d)

        cvzone.putTextRect(img,f'Depth:{int(d)}cm',(face[10][0]-80,face[10][1]-50),scale=1.85)

        for i,txt in enumerate(text):
            singleline=20+ int(d/2)
            # print(txt)
            scale= 0.5+ int((d/20)*10)/60 #hasasiat ro kam mikonim ba een tarfand {int((d/20)*10)/60} ashari grefte mishe
            cv.putText(ImgText,txt,(5,50+(i*singleline)),cv.FONT_ITALIC,scale,(255,255,255),2)
       

    stacked=cvzone.stackImages([img,ImgText],2,1)
    cv.imshow("webcam",stacked)
    if cv.waitKey(1) == ord ("s") : 
        break
    