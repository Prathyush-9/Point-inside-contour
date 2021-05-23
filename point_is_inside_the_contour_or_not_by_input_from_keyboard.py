import numpy as np
import cv2
import time
import imutils
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
color=(255,0,0)
thickness=3
#i=0
cap = cv2.VideoCapture(0)
ret, frame = cap.read()    #print(image)
#cv2.imwrite('image.png', image)
#image = mpimg.imread("image.png")
plt.imshow(frame)
plt.show()

while(True):
    ret, frame = cap.read()
    #frame = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
    frame = cv2.GaussianBlur(frame, (5,5), 0)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,90,90,cv2.THRESH_BINARY_INV)
    #thresh = np.float32(thresh)
    contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    #contours = np.float32(contours)
    
    x = input()
    y = input()
    for c in contours:
        dist = cv2.pointPolygonTest(c, (int(x) ,int(y)), False)
        if dist > 0:
            pt_color = (255 ,0, 0)
            img3 = frame
            cv2.circle(img3, (int(x),int(y)), 5, pt_color, -1)
            area = cv2.contourArea(c)
            if area > 10000:
                img3 = cv2.drawContours(img3, c, -1, (0,255,0), 3)
            cv2.imshow('Contours',img3)
            print('dist : ', dist)
            break

        elif dist < 0:
            pt_color = (0 ,255 ,0)
            img3 = frame
            img3 = cv2.circle(img3, (int(x),int(y)), 5, pt_color, -1)
            cv2.imshow('Contours',img3)
            print('dist : ', dist)
        #else:
            #pt_color = (128, 0, 128)

        #cv2.imshow("Cntours",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
cap.release()
cv2.destroyAllWindows()
