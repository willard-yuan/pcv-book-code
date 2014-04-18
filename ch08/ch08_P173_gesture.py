# -*- coding: utf-8 -*-
from PCV.localdescriptors import dsift
import os
from PCV.localdescriptors import sift
from pylab import *
from PCV.classifiers import knn

def get_imagelist(path):
    """    Returns a list of filenames for
        all jpg images in a directory. """

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.ppm')]

def read_gesture_features_labels(path):
    # create list of all files ending in .dsift
    featlist = [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.dsift')]
    # read the features
    features = []
    for featfile in featlist:
        l,d = sift.read_features_from_file(featfile)
        features.append(d.flatten())
    features = array(features)
    # create labels
    labels = [featfile.split('/')[-1][0] for featfile in featlist]
    return features,array(labels)

def print_confusion(res,labels,classnames):
    n = len(classnames)
    # confusion matrix
    class_ind = dict([(classnames[i],i) for i in range(n)])
    confuse = zeros((n,n))
    for i in range(len(test_labels)):
        confuse[class_ind[res[i]],class_ind[test_labels[i]]] += 1
    print 'Confusion matrix for'
    print classnames
    print confuse

filelist_train = get_imagelist('../data/gesture/train')
filelist_test = get_imagelist('../data/gesture/test')
imlist=filelist_train+filelist_test

# process images at fixed size (50,50)
for filename in imlist:
    featfile = filename[:-3]+'dsift'
    dsift.process_image_dsift(filename,featfile,10,5,resize=(50,50))

features,labels = read_gesture_features_labels('../data/gesture/train/')
test_features,test_labels = read_gesture_features_labels('../data/gesture/test/')
classnames = unique(labels)

# test kNN
k = 1
knn_classifier = knn.KnnClassifier(labels,features)
res = array([knn_classifier.classify(test_features[i],k) for i in
range(len(test_labels))])
# accuracy
acc = sum(1.0*(res==test_labels)) / len(test_labels)
print 'Accuracy:', acc

print_confusion(res,test_labels,classnames)
