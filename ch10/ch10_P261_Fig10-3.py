# -*- coding: utf-8 -*-
import cv2
import numpy
from pylab import *


# 读入图像
im = cv2.imread('../data/empire.jpg')
# 下采样
im_lowres = cv2.pyrDown(im)
# 转化为灰度图像
gray = cv2.cvtColor(im_lowres, cv2.COLOR_RGB2GRAY)
# 检测特征点
s = cv2.SURF()
mask = numpy.uint8(ones(gray.shape))
keypoints = s.detect(gray, mask)
# 显示图像及特征点
vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
for k in keypoints[::10]:
    cv2.circle(vis, (int(k.pt[0]), int(k.pt[1])), 2, (0, 255, 0), -1)
    cv2.circle(vis, (int(k.pt[0]), int(k.pt[1])), int(k.size), (0, 255, 0), 2)
cv2.imshow('local descriptors', vis)
cv2.waitKey()

cv2.imwrite('../images/ch10/ch10_P261_Fig10-3.jpg',vis)