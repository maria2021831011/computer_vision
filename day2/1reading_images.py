import cv2
image=cv2.imread('resources\lena.png')
print(image)

print(image.shape)
cv2.imshow('Output',image)
cv2.waitKey(0)