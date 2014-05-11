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
        # 载入图像列表
        self.path = './first500/'
        #self.path = 'D:/python_web/isoutu/first500/'
        self.imlist = [os.path.join(self.path,f) for f in os.listdir(self.path) if f.endswith('.jpg')]
        #self.imlist = get_imlist('./first500/')
        #self.imlist = get_imlist('E:/python/isoutu/first500/')
        self.nbr_images = len(self.imlist)
        self.ndx = range(self.nbr_images)

        # 载入词汇
        f = open('./first500/vocabulary.pkl', 'rb')
        self.voc = pickle.load(f)
        f.close()

        # 显示搜索返回的图像数
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
            #查询数据库，并获取前面的图像
            res = self.src.query(query)[:self.maxres]
            for dist, ndx in res:
                imname = self.src.get_filename(ndx)
                html += "<a href='?query="+imname+"'>"
                html += "<img src='"+imname+"' width='200' />"
                html += "</a>"
            # show random selection if no query
            # 如果没有查询图像则随机显示一些图像
        else:
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