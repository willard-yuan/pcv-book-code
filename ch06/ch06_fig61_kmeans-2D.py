# coding=utf-8
"""
Function:  figure 6.1
    An example of k-means clustering of 2D points
"""
from pylab import *
from scipy.cluster.vq import *

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

class1 = 1.5 * randn(100, 2)
class2 = randn(100, 2) + array([5, 5])
features = vstack((class1, class2))
centroids, variance = kmeans(features, 2)
code, distance = vq(features, centroids)
figure()
ndx = where(code == 0)[0]
plot(features[ndx, 0], features[ndx, 1], '*')
ndx = where(code == 1)[0]
plot(features[ndx, 0], features[ndx, 1], 'r.')
plot(centroids[:, 0], centroids[:, 1], 'go')

title(u'2维数据点聚类', fontproperties=font)
axis('off')
show()