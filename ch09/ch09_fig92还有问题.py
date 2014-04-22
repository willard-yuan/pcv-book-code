from scipy.misc import imresize
from PCV.tools import graphcut
from PIL import Image
from pylab import *

im = array(Image.open("../data/empire.jpg"))
im = imresize(im, 0.07)
size = im.shape[:2]

# add two rectangular training regions
labels = zeros(size)
labels[3:18, 3:18] = -1
labels[-18:-3, -18:-3] = 1

# create graph
g = graphcut.build_bayes_graph(im, labels, kappa=1)

# cut the graph
res = graphcut.cut_graph(g, size)

figure()
graphcut.show_labeling(im, labels)

figure()
imshow(res)
gray()
axis('off')
show()