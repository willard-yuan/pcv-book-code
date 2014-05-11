import pickle
from PCV.imagesearch import imagesearch
from PCV.localdescriptors import sift
from sqlite3 import dbapi2 as sqlite
from PCV.tools.imtools import get_imlist

imlist = get_imlist('./first500/')
nbr_images = len(imlist)
featlist = [imlist[i][:-3]+'sift' for i in range(nbr_images)]
# load vocabulary
with open('./first500/vocabulary.pkl', 'rb') as f:
    voc = pickle.load(f)
# create indexer
indx = imagesearch.Indexer('testImaAdd.db',voc)
indx.create_tables()
# go through all images, project features on vocabulary and insert
for i in range(nbr_images)[:500]:
    locs,descr = sift.read_features_from_file(featlist[i])
    indx.add_to_index(imlist[i],descr)
# commit to database
indx.db_commit()

con = sqlite.connect('testImaAdd.db')
print con.execute('select count (filename) from imlist').fetchone()
print con.execute('select * from imlist').fetchone()
