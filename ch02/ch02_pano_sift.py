import glob
import os
from PCV.localdescriptors import sift

for f in glob.glob('out/*.jpg'):
  base = os.path.splitext(os.path.basename(f))[0]
  siftpath = os.path.join('out', base + '.sift')
  if os.path.exists(siftpath):
      continue

  print 'processing', f
  sift.process_image(f, siftpath)