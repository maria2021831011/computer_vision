import cv2
img=cv2.imread('resources\lena.png')
img_horizontal=cv2.hconcat([img,img])
img_vertical=cv2.vconcat([img,img])
cv2.imshow('Horizontal Image',img_horizontal)
cv2.imshow('Vertical Image',img_vertical)
cv2.waitKey(0)