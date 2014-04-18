# -*- coding: utf-8 -*-
import os
from PCV.localdescriptors import sift, dsift
from pylab import  *
from PIL import Image

imlist=['../data/gesture/train/A-uniform01.ppm','../data/gesture/train/B-uniform01.ppm',
        '../data/gesture/train/C-uniform01.ppm','../data/gesture/train/Five-uniform01.ppm',
        '../data/gesture/train/Point-uniform01.ppm','../data/gesture/train/V-uniform01.ppm']

figure()
for i, im in enumerate(imlist):
    dsift.process_image_dsift(im,im[:-3]+'.dsift',90,40,True)
    l,d = sift.read_features_from_file(im[:-3]+'dsift')
    dirpath, filename=os.path.split(im)
    im = array(Image.open(im))
    #显示手势含义title
    titlename=filename[:-14]
    subplot(2,3,i+1)
    sift.plot_features(im,l,True)
    title(titlename)
show()