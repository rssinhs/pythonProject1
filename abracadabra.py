import cv2
import numpy as np
import time


cap=cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 16000)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 16000)



time.sleep(2)

background= 0

#capturingbackground
for i in range(30):
    ret, background = cap.read()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_videox.avi', fourcc, 20.0, size)


while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red= np.array([0,90,20])
    upper_red = np.array([2, 255, 255])


    mask1= cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([140, 90, 20])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1+mask2

    mask1= cv2.morphologyEx(mask1, cv2.MORPH_OPEN,np.ones((23,28),np.uint8),iterations=1)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((23,28), np.uint8), iterations=2)

    mask2= cv2.bitwise_not(mask1)

    res1= cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output= cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Eureka!',final_output)
    out.write(final_output)
    #k=cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
out.release()
cv2.destroyAllWindows()
