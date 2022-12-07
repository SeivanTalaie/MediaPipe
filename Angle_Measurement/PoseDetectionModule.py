import cv2 as cv
import mediapipe as mp
import time
import math



red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)



class PoseDetector():
    def __init__(self,mode=False,modelCO=1,smoothLMS=True,enableSEG=False,smoothSEG=True,detectionCON=0.5,trackingCON=0.5) :
        self.mode=mode
        self.modelCO=modelCO
        self.smoothLMS=smoothLMS
        self.enableSEG=enableSEG
        self.smoothSEG=smoothSEG
        self.detectionCON=detectionCON
        self.trackingCON=trackingCON  
        self.mediahands=mp.solutions.pose
        self.pose=self.mediahands.Pose(self.mode,self.modelCO,self.smoothLMS,self.enableSEG,self.smoothSEG,self.detectionCON,self.trackingCON)
        self.Draw=mp.solutions.drawing_utils



    def findPose(self,frame):
        RGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        self.results=self.pose.process(RGB)
        if self.results.pose_landmarks:
            self.Draw.draw_landmarks(frame,self.results.pose_landmarks,self.mediahands.POSE_CONNECTIONS)
        return frame



    def findposition(self,frame,draw=False):
        self.landmarklist=[]
        if self.results.pose_landmarks:
             for id,lm in enumerate(self.results.pose_landmarks.landmark):
                # print(id,lm)
                h,w,c=frame.shape
                x,y=int(lm.x*w),int(lm.y*h)
                self.landmarklist.append([id,x,y])
                # print(f'id : {id}, x : {x}, y : {y}',sep=("\n"))
        
            
                if draw:
                    # cv.rectangle(frame,(x,y),(x+w,y+h),blue,2)
                    cv.circle(frame,(x,y),6,red,-1)  #-1 means filled
        return self.landmarklist



    def findAngle(self,frame,p1,p2,p3,draw=False):
        x1,y1=self.landmarklist[p1][1:]   #_,x1,y1=self.landmarklist[p3]     also this one can be used
        x2,y2=self.landmarklist[p2][1:]
        x3,y3=self.landmarklist[p3][1:]


        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle<0:
            angle-=360
        
        # angle-=360
        # angle*=-1


        if draw :
            cv.circle(frame,(x1,y1),10,green,-1)  #-1 means filled
            cv.circle(frame,(x1,y1),20,green,2)  #-1 means filled 

            cv.line(frame,(x1,y1),(x2,y2),red,2)

            cv.circle(frame,(x2,y2),10,green,-1)  #-1 means filled
            cv.circle(frame,(x2,y2),20,green,2)  #-1 means filled

            cv.line(frame,(x2,y2),(x3,y3),red,2)

            cv.circle(frame,(x3,y3),10,green,-1)  #-1 means filled
            cv.circle(frame,(x3,y3),20,green,2)  #-1 means filled

            # cv.putText(frame,str(int(angle)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)

        return angle
              
    




def main():

    cap =cv.VideoCapture(0)
    ctime=0
    ptime=0
    cap.set(3,2000) # for resizing webcam window  ( width )
    cap.set(4,2000) # for resizing webcam window  ( hight )
    detector=PoseDetector()

    while True:
        _,frame=cap.read()
        frame=cv.resize(frame,(1600,1000))
        img=detector.findPose(frame)
        list=detector.findposition(frame,draw=True)
        angle=detector.findAngle(frame,12,14,16,draw=True)
        
        print(list)
        angles=detector.findAngle(frame,11,13,15,draw=True)
        print(angles)



        cv.imshow('webcam',frame)
        ctime=time.time()
        FPS= 1 / (ctime-ptime)
        ptime=ctime
        cv.putText(frame,str(int(FPS)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,red,2)
        if cv.waitKey(1)==ord('s'):
            break







if __name__=='__main__':
    main()