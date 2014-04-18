# coding=utf-8
"""
Function: figure 6.4
    Clustering of pixels based on their color value using k-means.
"""
from scipy.cluster.vq import *
from scipy.misc import imresize
from pylab import *
import Image

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

steps = 100  # image is divided in steps*steps region
infile = '../data/empire.jpg'
im = array(Image.open(infile))
dx = im.shape[0] / steps
dy = im.shape[1] / steps
# compute color features for each region
features = []
for x in range(steps):
    for y in range(steps):
        R = mean(im[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 0])
        G = mean(im[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 1])
        B = mean(im[x * dx:(x + 1) * dx, y * dy:(y + 1) * dy, 2])
        features.append([R, G, B])
features = array(features, 'f')     # make into array
# cluster
centroids, variance = kmeans(features, 3)
code, distance = vq(features, centroids)
# create image with cluster labels
codeim = code.reshape(steps, steps)
codeim = imresize(codeim, im.shape[:2], 'nearest')

figure()
ax1 = subplot(121)
title(u'原图', fontproperties=font)
#ax1.set_title('Image')
axis('off')
imshow(im)

ax2 = subplot(122)
title(u'聚类后的图像', fontproperties=font)
#ax2.set_title('Image after clustering')
axis('off')
imshow(codeim)

show()