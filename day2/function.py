import cv2
img=cv2.imread('resources\lena.png')
cv2.imshow('Image',img)

gary_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',gary_img)

blur_img=cv2.GaussianBlur(gary_img,(7,7),0)
cv2.imshow('Blur Image',blur_img)
edge_img=cv2.Canny(blur_img,50,150)
cv2.imshow('Edge Image',edge_img)
cv2.waitKey (0)