import cv2 as cv
import mediapipe as mp
import time
red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)

cap =cv.VideoCapture(0)

# cap.set(3,1600) # for resizing webcam window  ( width )
# cap.set(4,1500) # for resizing webcam window  ( hight )

mpfacedetection=mp.solutions.face_detection
face=mpfacedetection.FaceDetection()
Draw=mp.solutions.drawing_utils

ctime=0
ptime=0
while True:
    _,frame=cap.read()
    frame=cv.resize(frame,(1200,800))
    RGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=face.process(RGB)
    # print(results.multi_hand_landmarks)
    if results.detections:
        for id,lm in enumerate(results.detections):
            # Draw.draw_detection(frame,lm,mpfacedetection)
            print(id,lm)
            bbx1=lm.location_data.relative_bounding_box
            hi,wi,c=frame.shape 
            x,y,w,h= int ( bbx1.xmin * wi),int ( bbx1.ymin * hi),int ( bbx1.width * wi),int ( bbx1.height * hi)
            cv.rectangle(frame,(x,y),(x+w,y+h),red,2 )
            cv.putText(frame,f'{int(lm.score[0]*100)} %',(x,y),cv.FONT_HERSHEY_COMPLEX,2,blue,2)
   
    ctime=time.time()
    FPS= 1 / (ctime-ptime)
    ptime=ctime
    cv.putText(frame,str(int(FPS)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,red,2)
    cv.imshow('webcam',frame)
    if cv.waitKey(1)==ord('s'):
        break





