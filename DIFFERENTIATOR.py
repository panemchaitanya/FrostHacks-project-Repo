"""The program of the system S.A.P.P.H.I.R.E. used to interface the differntiation of the hands from each other"""

#importing the required modules
import cv2
from cvzone.HandTrackingModule import HandDetector #optimization command error shown in interface

#landmarks detection of the lands for recognition
detector = HandDetector(detectionCon=0.9, maxHands=1)

#landmarks comuation for the identification
cap = cv2.VideoCapture(0)
cam_w, cam_h = 640,480
cap.set(3, cam_w)
cap.set(4, cam_h)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img , flipType=False)
    
    #camera feed and wait close
    cv2.imshow("Camera Feed", img)
    cv2.waitKey(1)