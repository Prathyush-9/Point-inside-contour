import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils
cap = cv2.VideoCapture(0)
cap.set(10, 25)# for less brightness.
zap = 0
while(True):
    ret, frame = cap.read()
    #frame = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE) #if u want to read the stored image.
    blur = cv2.GaussianBlur(frame, (5,5), 0)
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,90,90,cv2.THRESH_BINARY_INV)
    contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    def mouse_callback(event, x, y ,flags, param):
        global contours, zap
        if event == cv2.EVENT_LBUTTONUP:
            for c in contours:
                if zap != 0:
                    dist = cv2.pointPolygonTest(c, (int(x) ,int(y)), False)
                    if dist > 0:
                        pt_color = (255 ,0, 0)
                        img3 = frame
                        cv2.circle(img3, (int(x),int(y)), 5, pt_color, -1)
                        img3 = cv2.drawContours(img3, c, -1, (0,255,0), 3)
                        x,y,w,h = cv2.boundingRect(c)
                        img4 = cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),2)
                        cv2.imshow('Contours',img3)
                        cv2.imshow('Contours',img4)
                        print('dist : ', dist)
                        break
                    elif dist < 0:
                        pt_color = (0 ,255 ,0)
                        img3 = frame
                        img3 = cv2.circle(img3, (int(x),int(y)), 5, pt_color, -1)
                        cv2.imshow('Contours',img3)
                        print('dist : ', dist)
                zap = zap + 1
            zap = 0
    cv2.namedWindow('Contours')
    cv2.setMouseCallback('Contours', mouse_callback)
    '''while(True):
        k = cv2.waitKey(1)                      #need it if u want to know where the previous points u have kept.
        if k == ord('m'):
            meaesure = not True
        elif k == 27:
            break'''
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
cap.release()
cv2.destroyAllWindows()
