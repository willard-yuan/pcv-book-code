 # -*- coding: utf-8 -*-
from PIL import Image
from pylab import *

im = array(Image.open('../data/empire.jpg'))
print im.shape, im.dtype
im = array(Image.open('../data/empire.jpg').convert('L'),'f')
print im.shape, im.dtype