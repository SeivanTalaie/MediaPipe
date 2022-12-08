import cv2 as cv
import cvzone 
from cvzone.FaceMeshModule import FaceMeshDetector
blue=(255,0,0)
red=(0,0,255)

cap= cv.VideoCapture(0)
cap.set(3,1800)
cap.set(4,1800)
detector=FaceMeshDetector(maxFaces=1)

while True : 
    _,img=cap.read()

    img,faces=detector.findFaceMesh(img,draw=False)

    if faces :
        face=faces[0]
        pointLeft=face[145]
        pointRight=face[374]
        # cv.line(img,pointLeft,pointRight,blue,3)
        # cv.circle(img,pointLeft,5,red,-1)
        # cv.circle(img,pointRight,5,red,-1)

        w,_=detector.findDistance(pointLeft,pointRight)
        # print(w)
        W=6.3
        # d=50 
        # f=(w*d)/W
        # print(f)



        f=720
        d=(W*f)/w
        print(d)

        cvzone.putTextRect(img,f'Depth:{int(d)}cm',(face[10][0]-80,face[10][1]-50),scale=1.85)

        


    cv.imshow("webcam",img)
    if cv.waitKey(1) == ord ("s") : 
        break
    