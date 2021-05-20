import cv2
import numpy as np
def empty(a):
    pass

#path='C:\Users\rssin\Downloads\lamborghini.png'
cv2.namedWindow('HSV_TRACKBAR')
cv2.resizeWindow('HSV_TRACKBAR',640,240)
cv2.createTrackbar('Hue_min','HSV_TRACKBAR',0,179,empty)
cv2.createTrackbar('Hue_max','HSV_TRACKBAR',179,179,empty)
cv2.createTrackbar('Sat_min','HSV_TRACKBAR',0,255,empty)
cv2.createTrackbar('Sat_max','HSV_TRACKBAR',255,255,empty)
cv2.createTrackbar('Value_min','HSV_TRACKBAR',0,255,empty)
cv2.createTrackbar('Value_max','HSV_TRACKBAR',0,255,empty)

while True:
    img  = cv2.imread('C:\\Users\\rssin\\Downloads\\lamborghini.png')
    #print(img.shape)
    imgresize=cv2.resize(img,(300,300))
    imghsv=cv2.cvtColor(imgresize,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos('Hue_min','HSV_TRACKBAR')
    h_max = cv2.getTrackbarPos('Hue_max', 'HSV_TRACKBAR')
    s_min = cv2.getTrackbarPos('Sat_min', 'HSV_TRACKBAR')
    s_max = cv2.getTrackbarPos('Sat_max', 'HSV_TRACKBAR')
    v_min = cv2.getTrackbarPos('Value_min', 'HSV_TRACKBAR')
    v_max = cv2.getTrackbarPos('Value_max', 'HSV_TRACKBAR')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower= np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imghsv,lower,upper)
    imgResult=cv2.bitwise_and(imgresize,imgresize,mask=mask)

    cv2.imshow('DreamCar', imghsv)
    cv2.imshow('Dream Car', imgresize)
    cv2.imshow('mask', mask)
    cv2.imshow('m',imgResult )


    cv2.waitKey(1)


