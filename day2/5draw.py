import cv2
import numpy as np
canvas=np.zeros((512,512,3),dtype='uint8')
canvas.fill(255)
li=cv2.line(canvas,(0,0),(511,511),(255,0,0),5)

cv2.rectangle(canvas,(384,0),(510,128),(0,255,0),3)
cv2.circle(canvas,(447,63),63,(0,0,255),-1)
cv2.ellipse(canvas,(256,256),(100,50),0,0,180,255,-1)
cv2.putText(canvas,'OpenCV',(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,0),2)
cv2.imshow('Drawing',canvas)
cv2.waitKey(0)