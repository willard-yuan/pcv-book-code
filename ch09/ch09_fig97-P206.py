from PCV.tools import rof
from pylab import *
from PIL import Image
import scipy.misc



#im = array(Image.open('../data/ceramic-houses_t0.png').convert("L"))
im = array(Image.open('../data/flower32_t0.png').convert("L"))
figure()
gray()
subplot(131)
axis('off')
imshow(im)

U, T = rof.denoise(im, im, tolerance=0.001)
subplot(132)
axis('off')
imshow(U)

#t = 0.4  # ceramic-houses_t0 threshold
t = 0.8  # flower32_t0 threshold
seg_im = U < t*U.max()
#scipy.misc.imsave('ceramic-houses_t0_result.pdf', seg_im)
scipy.misc.imsave('flower32_t0_result.pdf', seg_im)
subplot(133)
axis('off')
imshow(seg_im)

show()