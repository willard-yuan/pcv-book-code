# -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from scipy.ndimage import measurements, morphology
from pylab import *

"""   This is the morphology counting objects example in Section 1.4.  """

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

# load image and threshold to make sure it is binary
figure()
gray()
im = array(Image.open('../data/houses.png').convert('L'))
subplot(221)
imshow(im)
axis('off')
title(u'原图', fontproperties=font)
im = (im < 128)

labels, nbr_objects = measurements.label(im)
print "Number of objects:", nbr_objects
subplot(222)
imshow(labels)
axis('off')
title(u'标记后的图', fontproperties=font)

# morphology - opening to separate objects better
im_open = morphology.binary_opening(im, ones((9, 5)), iterations=2)
subplot(223)
imshow(im_open)
axis('off')
title(u'开运算后的图像', fontproperties=font)

labels_open, nbr_objects_open = measurements.label(im_open)
print "Number of objects:", nbr_objects_open
subplot(224)
imshow(labels_open)
axis('off')
title(u'开运算后进行标记后的图像', fontproperties=font)

show()