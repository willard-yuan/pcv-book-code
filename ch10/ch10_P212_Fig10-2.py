# -*- coding: utf-8 -*-
import cv2
import numpy
from pylab import *


# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

# 读入图像
filename = '../data/fisherman.jpg'
im = cv2.imread(filename)
# 转换颜色空间
rgbIm = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# 显示原图
fig = plt.figure()
subplot(121)
plt.gray()
imshow(rgbIm)
title(u'原图', fontproperties=font)
axis('off')

# 获取图像尺寸
h, w = im.shape[:2]
# 泛洪填充
diff = (6, 6, 6)
mask = zeros((h+2, w+2), numpy.uint8)
cv2.floodFill(im, mask, (10, 10), (255, 255, 0), diff, diff)

# 显示泛洪填充后的结果
subplot(122)
imshow(im)
title(u'泛洪填充', fontproperties=font)
axis('off')

show()
#fig.savefig("../images/ch10/floodFill.png")

# 在OpenCV窗口中显示泛洪填充后的结果
# cv2.imshow('flood fill', im)
# cv2.waitKey()
# 保存结果
# cv2.imwrite('../images/ch10/floodFill.jpg',im)