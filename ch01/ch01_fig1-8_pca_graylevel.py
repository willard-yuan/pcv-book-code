 # -*- coding: utf-8 -*-
import pickle
from PIL import Image
from numpy import *
from pylab import *
from PCV.tools import imtools, pca

# Uses sparse pca codepath.
#imlist = imtools.get_imlist('../data/selectedfontimages/a_selected_thumbs')

# 获取图像列表和他们的尺寸
imlist = imtools.get_imlist('../data/fontimages/a_thumbs')  # fontimages.zip is part of the book data set
im = array(Image.open(imlist[0]))  # open one image to get the size
m, n = im.shape[:2]  # get the size of the images
imnbr = len(imlist)  # get the number of images
print "The number of images is %d" % imnbr

# Create matrix to store all flattened images
immatrix = array([array(Image.open(imname)).flatten() for imname in imlist], 'f')

# PCA降维
V, S, immean = pca.pca(immatrix)

# 保存均值和主成分
f = open('../data/fontimages/font_pca_modes.pkl', 'wb')
pickle.dump(immean,f)
pickle.dump(V,f)
f.close()

# Show the images (mean and 7 first modes)
# This gives figure 1-8 (p15) in the book.
figure()
gray()
subplot(2, 4, 1)
axis('off')
imshow(immean.reshape(m, n))
for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))
    axis('off')
show()
