import cv2 as cv
import mediapipe as mp
import time
red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)

cap =cv.VideoCapture(0)

cap.set(3,720) # for resizing webcam window  ( width )
cap.set(4,480) # for resizing webcam window  ( hight )

mediaface=mp.solutions.face_mesh
face=mediaface.FaceMesh()
Draw=mp.solutions.drawing_utils
draw_spec= Draw.DrawingSpec()

ctime=0
ptime=0
while True:
    _,frame=cap.read()
    # frame=cv.resize(frame,(1600,1000))
    RGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=face.process(RGB)
    # print(results.multi_face_landmarks)
    if results.multi_face_landmarks:
        for facemesh in results.multi_face_landmarks:

            Draw.draw_landmarks(frame,facemesh)
            for id,lm in enumerate(facemesh.landmark):
                # print(lm)
                h,w,c=frame.shape
                x,y=int(lm.x*w),int(lm.y*h)
                print(f'id : {id}, x : {x}, y : {y}',sep=("\n"))
                # if id:
                #     cv.rectangle(frame,(x,y),(x+w,y+h),blue,2)
                #     cv.circle(frame,(x,y),3,green,-1)  #-1 means filled
    
    ctime=time.time()
    FPS= 1 / (ctime-ptime)
    ptime=ctime
    cv.putText(frame,str(int(FPS)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,red,2)
    cv.imshow('webcam',frame)
    if cv.waitKey(1)==ord('s'):
        break





