import cv2
resize_img=cv2.imread('resources\lena.png')
resized_image=cv2.resize(resize_img,(300,300))
cv2.imshow('Resized Image',resized_image)
croped_image=resize_img[100:400,100:400]
cv2.imshow('Croped Image',croped_image)
cv2.waitKey(0)