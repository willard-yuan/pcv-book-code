from scipy import *
import cv2

# setup video capture
cap = cv2.VideoCapture(0)
cap.open(0)
if cap.isOpened():
  print "Finally"
else:
  print "BOOM"
frames = []
# get frame, store in array
while True:
    ret, im = cap.read()
    cv2.imshow('video', im)
    frames.append(im)
    if cv2.waitKey(10) == 27:
      break
frames = array(frames)
# check the sizes
print im.shape
print frames.shape