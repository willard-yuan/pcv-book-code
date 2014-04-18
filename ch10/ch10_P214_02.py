import cv2

# setup video capture
cap = cv2.VideoCapture(0)
cap.open(0)
# get frame, apply Gaussian smoothing, show result
while True:
    ret, im = cap.read()
    blur = cv2.GaussianBlur(im, (0, 0), 5)
    cv2.imshow('camera blur', blur)
    if cv2.waitKey(10) == 27:
      break