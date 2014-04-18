# -*- coding: utf-8 -*-
import cv2
from pylab import *


# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

# 读入图像
im = cv2.imread('../data/fisherman.jpg')
# 转换颜色空间
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 显示积分图像
fig = plt.figure()
subplot(121)
plt.gray()
imshow(gray)
title(u'灰度图', fontproperties=font)
axis('off')

# 计算积分图像
intim = cv2.integral(gray)
# 归一化
intim = (255.0*intim) / intim.max()

#显示积分图像
subplot(122)
plt.gray()
imshow(intim)
title(u'积分图', fontproperties=font)
axis('off')
show()

# 用OpenCV显示图像
#cv2.imshow("Image", intim)
#cv2.waitKey()

# 用OpenCV保存积分图像
#cv2.imwrite('../images/ch10/ch10_P211_Displaying-Images-and-Results-cv2.jpg',intim)

# 保存figure中的灰度图像和积分图像
#fig.savefig("../images/ch10/ch10_P211_Displaying-Images-and-Results.png")