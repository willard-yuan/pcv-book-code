 # -*- coding: utf-8 -*-
from PIL import Image
from numpy import *
from pylab import *

im = array(Image.open('../data/empire.jpg').convert('L'))
print int(im.min()), int(im.max())

im2 = 255 - im  # invert image
print int(im2.min()), int(im2.max())

im3 = (100.0/255) * im + 100  # clamp to interval 100...200
print int(im3.min()), int(im3.max())

im4 = 255.0 * (im/255.0)**2  # squared
print int(im4.min()), int(im4.max())

figure()
gray()
subplot(1, 3, 1)
imshow(im2)
axis('off')
title(r'$f(x)=255-x$')

subplot(1, 3, 2)
imshow(im3)
axis('off')
title(r'$f(x)=\frac{100}{255}x+100$')

subplot(1, 3, 3)
imshow(im4)
axis('off')
title(r'$f(x)=255(\frac{x}{255})^2$')
show()