import lktrack

imnames = ['../data/bt/bt.003.pgm', '../data/bt/bt.002.pgm', '../data/bt/bt.001.pgm', '../data/bt/bt.000.pgm']
# create tracker object
lkt = lktrack.LKTracker(imnames)
# detect in first frame, track in the remaining
lkt.detect_points()
lkt.draw()
for i in range(len(imnames)-1):
    lkt.track_points()
    lkt.draw()