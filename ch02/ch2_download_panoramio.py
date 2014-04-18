# -*- coding: utf-8 -*-
import json
import os
import urllib
import urlparse

#change the longitude and latitude here
#here is the longitude and latitude for Oriental Pearl
minx = '-77.037564'
maxx = '-77.035564'
miny = '38.896662'
maxy = '38.898662'

#number of photos
numfrom = '0'
numto = '20'
url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&from=' + numfrom + '&to=' + numto + '&minx=' + minx + '&miny=' + miny + '&maxx=' + maxx + '&maxy=' + maxy + '&size=medium'

#this is the url configured for downloading whitehouse photos. Uncomment this, run and see.
#url = 'http://www.panoramio.com/map/get_panoramas.php?order=popularity&set=public&from=0&to=20&minx=-77.037564&miny=38.896662&maxx=-77.035564&maxy=38.898662&size=medium'

c = urllib.urlopen(url)

j = json.loads(c.read())
imurls = []
for im in j['photos']:
    imurls.append(im['photo_file_url'])

for url in imurls:
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
    print 'downloading:', url