import cv2
import numpy as np
import time
import playsound

def playaudio():
 playsound.playsound('C:\\Users\\rssin\\Downloads\\alarm1.wav', True)
fire_reported=0
status=False

def biggestContourI(contours):
    maxVal = 0
    maxI = None
    for i in range(0, len(contours) - 1):
        if len(contours[i]) > maxVal:
            cs = contours[i]
            maxVal = len(contours[i])
            maxI = i
    return maxI


pipe="C:\\Users\\rssin\\Downloads\\fire.mp4"

cap=cv2.VideoCapture(pipe)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_videox.avi', fourcc, 20.0, size)

while(cap.isOpened()):
    ret, frame= cap.read()
    blur=cv2.GaussianBlur(frame,(25,25),0)
    hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower= [10,50,50]
    upper=[20,255,255]
    lower=np.array(lower,dtype='uint8')
    upper = np.array(upper, dtype='uint8')
    mask=cv2.inRange(hsv,lower,upper)

    output=cv2.bitwise_and(frame,hsv,mask=mask)
    contours0, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    number=cv2.countNonZero(mask)


    if 11000 < int(number) < 25000:
        print('fire')
        playaudio()
        cv2.putText(frame,
                    'Fire',
                    (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255),
                    2,
                    cv2.LINE_4)
    if int(number) >25000:
        print('high fire')
        playaudio()
        cv2.putText(frame,
                    'High Fire',
                    (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255),
                    2,
                    cv2.LINE_4)
    if ret == False:
        break
    bc = biggestContourI(contours0)
    cv2.drawContours(frame, contours0, bc, (0, 255, 0), 5)
    cv2.putText(frame,
                str(number),
                (70, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (11, 255, 255),
                2,
                cv2.LINE_4)

    cv2.imshow('output', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
