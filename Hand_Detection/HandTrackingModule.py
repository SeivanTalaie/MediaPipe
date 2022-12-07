import cv2 as cv
import mediapipe as mp
import time

red=(0,0,255)
blue=(255,0,0)
green=(0,255,0)

class handDetector():
    def __init__(self,mode=False,handno=2,modelcomplexity=1,detectionCon=0.5,trackingCon=0.5):
               self.mode=mode
               self.handno=handno
               self.modelcomplexity=modelcomplexity
               self.detectionCon=detectionCon
               self.trackingCon=trackingCon

               self.mediahands=mp.solutions.hands
               self.hands=self.mediahands.Hands(self.mode , self.handno,self.modelcomplexity,self.detectionCon,self.trackingCon)
               self.Draw=mp.solutions.drawing_utils
                    

    def findHands(self,frame,draw=True):
        RGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        self.results=self.hands.process(RGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlandmark in self.results.multi_hand_landmarks:
                if draw:
                   self.Draw.draw_landmarks(frame,handlandmark,self.mediahands.HAND_CONNECTIONS)
        return frame       


    def findposition(self,frame,handNo=0 , draw=True):
        landmarklist=[]

        if self.results.multi_hand_landmarks:
            myhand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                # print(id,lm)
                h,w,c=frame.shape
                x,y=int(lm.x*w),int(lm.y*h)
                # print(f'id : {id}, x : {x}, y : {y}',sep=("\n"))
                landmarklist.append([id,x,y])

                if draw:
                    # cv.rectangle(frame,(x,y),(x+w,y+h),blue,2)
                    cv.circle(frame,(x,y),12,green,-1)  #-1 means filled
        return landmarklist

 
def main():
    ctime=0
    ptime=0
    cap =cv.VideoCapture(0)
    detector=handDetector()
    
    while True:
        _,frame=cap.read()
        frame=detector.findHands(frame)
        list=detector.findposition(frame)
        if len(list) != 0:
            print(list)
        ctime=time.time()
        FPS= 1 / (ctime-ptime)
        ptime=ctime
        cv.putText(frame,str(int(FPS)),(100,100),cv.FONT_HERSHEY_COMPLEX,2,red,2)
        cv.imshow('webcam',frame)
        if cv.waitKey(10)==ord('s'):
            break


if __name__ == '__main__':
    main()