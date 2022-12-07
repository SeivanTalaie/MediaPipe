import cv2 as cv
import mediapipe as mp
import time
red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)

cap =cv.VideoCapture(0)
mediahands=mp.solutions.hands
hands=mediahands.Hands()
Draw=mp.solutions.drawing_utils

ctime=0
ptime=0
while True:
    _,frame=cap.read()
    RGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=hands.process(RGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark):
                # print(id,lm)
                h,w,c=frame.shape
                x,y=int(lm.x*w),int(lm.y*h)
                print(f'id : {id}, x : {x}, y : {y}',sep=("\n"))
                Draw.draw_landmarks(frame,handlandmark,mediahands.HAND_CONNECTIONS)
                if id:
                    # cv.rectangle(frame,(x,y),(x+w,y+h),blue,2)
                    cv.circle(frame,(x,y),10,green,-1)  #-1 means filled
    
    ctime=time.time()
    FPS= 1 / (ctime-ptime)
    ptime=ctime
    cv.putText(frame,str(int(FPS)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,red,2)
    cv.imshow('webcam',frame)
    if cv.waitKey(10)==ord('s'):
        break





