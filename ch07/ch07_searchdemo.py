# -*- coding: utf-8 -*-
import cherrypy
import pickle
import urllib
import os
from numpy import *
#from PCV.tools.imtools import get_imlist
from PCV.imagesearch import imagesearch

"""
This is the image search demo in Section 7.6.
"""


class SearchDemo:

    def __init__(self):
        # load list of images
        self.path = './first500/'
        #self.path = 'D:/python_web/isoutu/first500/'
        self.imlist = [os.path.join(self.path,f) for f in os.listdir(self.path) if f.endswith('.jpg')]
        #self.imlist = get_imlist('./first500/')
        #self.imlist = get_imlist('E:/python/isoutu/first500/')
        self.nbr_images = len(self.imlist)
        self.ndx = range(self.nbr_images)

        # load vocabulary
        f = open('./first500/vocabulary.pkl', 'rb')
        self.voc = pickle.load(f)
        f.close()

        # set max number of results to show
        self.maxres = 49

        # header and footer html
        self.header = """
            <!doctype html>
            <head>
            <title>Image search</title>
            </head>
            <body>
            """
        self.footer = """
            </body>
            </html>
            """

    def index(self, query=None):
        self.src = imagesearch.Searcher('testImaAdd.db', self.voc)

        html = self.header
        html += """
            <br />
            Click an image to search. <a href='?query='> Random selection </a> of images.
            <br /><br />
            """
        if query:
            # query the database and get top images
            res = self.src.query(query)[:self.maxres]
            for dist, ndx in res:
                imname = self.src.get_filename(ndx)
                html += "<a href='?query="+imname+"'>"
                html += "<img src='"+imname+"' width='200' />"
                html += "</a>"
        else:
            # show random selection if no query
            random.shuffle(self.ndx)
            for i in self.ndx[:self.maxres]:
                imname = self.imlist[i]
                html += "<a href='?query="+imname+"'>"
                html += "<img src='"+imname+"' width='200' />"
                html += "</a>"

        html += self.footer
        return html

    index.exposed = True

#conf_path = os.path.dirname(os.path.abspath(__file__))
#conf_path = os.path.join(conf_path, "service.conf")
#cherrypy.config.update(conf_path)
#cherrypy.quickstart(SearchDemo())

cherrypy.quickstart(SearchDemo(), '/', config=os.path.join(os.path.dirname(__file__), 'service.conf'))