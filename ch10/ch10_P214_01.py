import cv2

# setup video capture
cap = cv2.VideoCapture(0)
cap.open(0)
while True:
    ret,im = cap.read()
    cv2.imshow('video test',im)
    key = cv2.waitKey(10)
    if key == 27:
        break