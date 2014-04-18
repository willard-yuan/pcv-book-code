from PIL import Image
from pylab import *
from scipy.ndimage import filters
#from SciPy import misc
from PCV.tools import imtools

im = array(Image.open('../data/empire.jpg').convert('L'))
#im = misc.lena()
im2, cdf = imtools.histeq(im)
im3 = np.uint8(255 * (im / (filters.gaussian_filter(im, 400) + 0.00001)))

figure()
subplot(231)
axis('off')
gray()
title('original')
imshow(im)

subplot(234)
axis('off')
title('original hist')
#hist(im.flatten(), 128, cumulative=True, normed=True)
hist(im.flatten(), 128, normed=True)

subplot(232)
axis('off')
gray()
title('histogram-equalized')
imshow(im2)

subplot(235)
axis('off')
title('equalized hist')
#hist(im2.flatten(), 128, cumulative=True, normed=True)
hist(im2.flatten(), 128, normed=True)

subplot(233)
axis('off')
gray()
title('quotient image')
imshow(im3)

subplot(236)
axis('off')
title('quotient hist')
hist(im3.flatten(), 128, normed=True)

show()
