import lktrack
from pylab import *
imnames = ['../data/viff/viff.000.ppm', '../data/viff/viff.001.ppm',
           '../data/viff/viff.002.ppm', '../data/viff/viff.003.ppm', '../data/viff/viff.004.ppm']
# track using the LKTracker generator
lkt = lktrack.LKTracker(imnames)
for im,ft in lkt.track():
    print 'tracking %d features' % len(ft)

# plot the tracks
figure()
imshow(im)
for p in ft:
    plot(p[0],p[1],'bo')
for t in lkt.tracks:
    plot([p[0] for p in t],[p[1] for p in t])
axis('off')
show()