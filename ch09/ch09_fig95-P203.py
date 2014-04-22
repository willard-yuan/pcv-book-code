from PCV.tools import ncut
from scipy.misc import imresize
from pylab import *
from PIL import Image

im = array(Image.open('C-uniform03.ppm'))
m, n = im.shape[:2]
# resize image to (wid,wid)
wid = 50
rim = imresize(im, (wid, wid), interp='bilinear')
rim = array(rim, 'f')
# create normalized cut matrix
A = ncut.ncut_graph_matrix(rim, sigma_d=1, sigma_g=1e-2)
# cluster
code, V = ncut.cluster(A, k=3, ndim=3)

imshow(imresize(V[i].reshape(wid,wid),(m,n),interp='bilinear'))