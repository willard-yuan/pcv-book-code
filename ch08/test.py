# -*- coding: utf-8 -*-
from PIL import Image
from pylab import *
from scipy.ndimage import measurements


def find_sudoku_edges(im, axis=0):
    """ 寻找对齐后数独图像的的单元边线 """
    # threshold and sum rows and columns
    #阈值化，像素值小于128的阈值处理后为1，大于128的为0
    trim = 1*(128 > im)
    #阈值处理后对行（列）相加求和
    s = trim.sum(axis=axis)
    print s
    # find center of strongest lines
    # 寻找连通区域
    s_labels, s_nbr = measurements.label((0.5*max(s)) < s)
    print s_labels
    print s_nbr
    #计算各连通域的质心
    m = measurements.center_of_mass(s, s_labels, range(1, s_nbr+1))
    print m
    #对质心取整，质心即为粗线条所在位置
    x = [int(x[0]) for x in m]
    print x
	# if only the strong lines are detected add lines in between
    # 如果检测到了粗线条，便在粗线条间添加直线
    if 4 == len(x):
        dx = diff(x)
        x = [x[0], x[0]+dx[0]/3, x[0]+2*dx[0]/3, x[1], x[1]+dx[1]/3, x[1]+2*dx[1]/3, x[2], x[2]+dx[2]/3, x[2]+2*dx[2]/3, x[3]]
    if 10 == len(x):
        return x
    else:
        raise RuntimeError('Edges not detected.')

imname = '../data/sudoku_images/sudoku_images/sudokus/sudoku18.jpg'
im = array(Image.open(imname).convert('L'))
print im.shape
figure()
gray()
imshow(im)
axis('off')

# find the cell edges
# 寻找x方向的单元边线
x = find_sudoku_edges(im, axis=0)
#寻找y方向的单元边线
y = find_sudoku_edges(im, axis=1)

figure()
gray()

y1=[y[0],y[3],y[6],y[-1]]
y2=[y[1],y[2],y[4],y[5],y[7],y[8]]

#画直线
for i, ch in enumerate(y1):
    x1 = range(x[0], x[-1]+1, 1)
    y1 = ch*ones(len(x1))
    #画散点图
    plot(x1, y1, 'r', linewidth=2)

for i, ch in enumerate(y2):
    x1 = range(x[0], x[-1]+1, 1)
    y1 = ch*ones(len(x1))
    #画散点图
    plot(x1, y1, 'b', linewidth=2)

'''for i, ch in enumerate(x):
    y1 = range(x[0], x[-1]+1, 1)
    x1 = ch*ones(len(x1))
    #画散点图
    plot(x1, y1, 'r', linewidth=2)

plot(x, y, 'or', linewidth=2)'''

imshow(im)
axis('off')
show()