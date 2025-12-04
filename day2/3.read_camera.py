import cv2
camera=cv2.VideoCapture(0)
while True:
    ret,frame=camera.read()
    if ret==False:
        break
    cv2.imshow('Camera',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break