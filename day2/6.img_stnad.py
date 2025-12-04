import cv2
import numpy as np
img=cv2.imread('resources\cards.jpg')
pts1=np.float32([[755,120],[1122,263],[520,678],[863,829]])
pts2=np.float32([[0,0],[300,0],[0,400],[300,400]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
result=cv2.warpPerspective(img,matrix,(300,400))
cv2.imshow('Image',img)
cv2.imshow('Output',result)
cv2.waitKey(0)