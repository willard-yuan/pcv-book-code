# -*- coding: utf-8 -*-
from PCV.localdescriptors import sift, dsift
from pylab import  *
from PIL import Image

dsift.process_image_dsift('../data/empire.jpg','empire.dsift',90,40,True)
l,d = sift.read_features_from_file('empire.dsift')
im = array(Image.open('../data/empire.jpg'))
sift.plot_features(im,l,True)
title('dense SIFT')
show()