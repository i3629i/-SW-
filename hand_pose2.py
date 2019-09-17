from __future__ import division
import numpy as np
import cv2
import time

hand_cascade = cv2.CascadeClassifier('hand3.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray,1.3,5)
    print(hand)
    if ret is False:
        exit()

    cv2.imshow('test',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllwindows()
