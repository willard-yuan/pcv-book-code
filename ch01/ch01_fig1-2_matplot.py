from PIL import Image
from pylab import *

im = array(Image.open('../data/empire.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')

plot(x[:2], y[:2])

#axis('off')

title('Plotting: "empire.jpg"')
show()
