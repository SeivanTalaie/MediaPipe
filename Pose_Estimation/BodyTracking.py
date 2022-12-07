import cv2 as cv
import mediapipe as mp 


red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)

cap= cv.VideoCapture(0) 
# cap.set(3,1000)
# cap.set(4,1000)
mpPose=mp.solutions.pose 
pose=mpPose.Pose()
draw=mp.solutions.drawing_utils


while True :
    _,frame = cap.read()
    resized=cv.resize(frame,(1600,1000))
    rgb=cv.cvtColor(resized,cv.COLOR_BGR2RGB)
    result=pose.process(rgb)
    # print(result.pose_landmarks)
    if result.pose_landmarks:
         for id,lm in enumerate(result.pose_landmarks.landmark):
                h,w,c=resized.shape 
                x,y=int(lm.x*w) , int(lm.y*h)
                print ( id , x , y )
                draw.draw_landmarks(resized,result.pose_landmarks,mpPose.POSE_CONNECTIONS)
                if id:
                    cv.circle(resized,(x,y), 10,blue,-1)
                

    cv.imshow('webcam',resized)
    if cv.waitKey(1) == ord ('s'):
        break