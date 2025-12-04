import cv2
video=cv2.VideoCapture('resources\elon.mp4')
while True:
    ret,frame=video.read()
    if ret==False:
        break
    cv2.imshow('Video',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break