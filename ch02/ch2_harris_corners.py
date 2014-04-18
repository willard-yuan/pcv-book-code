# -*- coding: utf-8 -*-
from pylab import *
from PIL import Image
from PCV.localdescriptors import harris

"""
Example of detecting Harris corner points (Figure 2-1 in the book).
"""

# 读入图像
im = array(Image.open('../data/empire.jpg').convert('L'))

# 检测harris角点
harrisim = harris.compute_harris_response(im)

# Harris响应函数
harrisim1 = 255 - harrisim

figure()
gray()

#画出Harris响应图
subplot(141)
imshow(harrisim1)
print harrisim1.shape
axis('off')
axis('equal')

threshold = [0.01, 0.05, 0.1]
for i, thres in enumerate(threshold):
    filtered_coords = harris.get_harris_points(harrisim, 6, thres)
    subplot(1, 4, i+2)
    imshow(im)
    print im.shape
    plot([p[1] for p in filtered_coords], [p[0] for p in filtered_coords], '*')
    axis('off')

#原书采用的PCV中PCV harris模块
#harris.plot_harris_points(im, filtered_coords)

# plot only 200 strongest
# harris.plot_harris_points(im, filtered_coords[:200])

show()