import os
import urllib
import urlparse
import json

URL = 'http://www.panoramio.com/map/get_panoramas.php?' \
      'order=popularity&set=public&size=medium&' \
      'from=20&to={n}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}'

# Santa cruz lighthouse: x=-122.026618 y=36.951614
# White house: x=-77.038564 y=38.897662

x = -122.026618
y = 36.951614
d = 0.001
url = URL.format(
    n=40, minx=x - d, miny=y - d, maxx=x + d, maxy=y + d)

j = json.loads(urllib.urlopen(url).read())
imurls = [im['photo_file_url'] for im in j['photos']]

for url in imurls:
  image = urllib.URLopener()
  base = os.path.basename(urlparse.urlparse(url).path)
  image.retrieve(url, os.path.join('out', base))
  print 'downloading', url
