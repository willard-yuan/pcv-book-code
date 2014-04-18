# -*- coding: utf-8 -*-
from PCV.tools.imtools import get_imlist
from PIL import Image
from pylab import *
from PCV.tools import imtools

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

filelist = get_imlist('../data/avg/') #获取convert_images_format_test文件夹下的图片文件名(包括后缀名)
avg = imtools.compute_average(filelist)

for impath in filelist:
        im1 = array(Image.open(impath))
        subplot(2, 2, filelist.index(impath)+1)
        imshow(im1)
        imNum=str(filelist.index(impath)+1)
        title(u'待平均图像'+imNum, fontproperties=font)
        axis('off')
subplot(2, 2, 4)
imshow(avg)
title(u'平均后的图像', fontproperties=font)
axis('off')

show()
