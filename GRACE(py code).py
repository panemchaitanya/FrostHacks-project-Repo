"""Gesture Robust Arduino Controller Equipment"""

'''Objective of the Project is to create a system which can controll any sort of Electronic Device Or Equipment using Arduino, Open CV and the concept of Leap Motion'''

#importing the required Python modules and libraries with extensions
import cv2
import mediapipe as mp
import time
import grace as cnt #(To be enabled when required to connect the 'Controller' program to the main input Program.)

#to be enables for EXCEL to update results
#import pandas as pd

#delaying the start by 2 seconds
time.sleep(2.0)

#drawing a solution for our hand which is required for the detection, which cointains all the hand connections
mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

#tip ID's of our fingers (refer figure 2 of the PPT.)
tipIds=[4,8,12,16,20] #20,16,12,8,4
video=cv2.VideoCapture(0)

#enabling the Computer vision to detect the Hand Gestures and drawing the Landmarks
with mp_hand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as hands:
    while True:
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList=[]
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    lmList.append([id,cx,cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers=[]
        if len(lmList)!=0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1,5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

#identifing the gestures from the Computer vision and converting them to the required signals, here to the count of fingers
            total=fingers.count(1)
            
            #code for EXCEL update to store results
            #p={'total LEDS':total}
            #n=pd.DataFrame(p)
            #n.to_csv(r"C:\Users\chint\Downloads\Test_data1.csv")

            cnt.led(total) #(To be enabled only when the 'Controller' program is enabled) 
            if total==0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "LED", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==1:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "Device", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==2:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "Device", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==3:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "Device", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==4:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "Device", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
            elif total==5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)
                cv2.putText(image, "Device", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 5)

#the above code simply shows that the system can identify the Gesture i.e., number of Fingers shown through the camera and as the proof of the identification the system shows the number of LEDS turned ON according to the number of fingers shown which is detailed in the 'Controller' code

        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
#exiting the Computer Vision by destroying/deleting the Terminal
video.release()
cv2.destroyAllWindows()

'''Due to the interlink of the 'main input Program' and the 'Controller' code so the ending of the both programs take place here'''