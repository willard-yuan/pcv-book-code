from PIL import Image
import glob
import numpy
import os
import pydot
from PCV.localdescriptors import sift

imlist = glob.glob('out/*.jpg')
siftlist = glob.glob('out/*.sift')
image_count = len(imlist)

cachefile = 'out_pano_match.txt'
if os.path.exists(cachefile):
  matchscores = numpy.loadtxt(cachefile)
else:
  matchscores = numpy.zeros((image_count, image_count))

  for i in range(image_count):
    for j in range(i, image_count):
      print 'comparing', imlist[i], imlist[j]
      l1, d1 = sift.read_features_from_file(siftlist[i])
      l2, d2 = sift.read_features_from_file(siftlist[j])
      matches = sift.match_twosided(d1, d2)
      match_count = sum(matches > 0)
      matchscores[i, j] = match_count

  for i in range(image_count):
    for j in range(i + 1, image_count):
      matchscores[j, i] = matchscores[i, j]

  numpy.savetxt(cachefile, matchscores, '%i')


threshold = 2
g = pydot.Dot(graph_type='graph')
for i in range(image_count):
  for j in range(i + 1, image_count):
    if matchscores[i, j] <= threshold:
      continue

    # Note: pydot needs absolute paths for the image= parameter.

    im = Image.open(imlist[i])
    im.thumbnail((300, 300))
    filename = 'out_pano_{}.png'.format(i)
    im.save(filename)
    g.add_node(pydot.Node(str(i), fontcolor='transparent',
      shape='rectangle', image=os.path.abspath(filename)))

    im = Image.open(imlist[j])
    im.thumbnail((300, 300))
    filename = 'out_pano_{}.png'.format(j)
    im.save(filename)
    g.add_node(pydot.Node(str(j), fontcolor='transparent',
      shape='rectangle', image=os.path.abspath(filename)))

    g.add_edge(pydot.Edge(str(i), str(j)))
g.write_png('out_lighthouse.png')
