# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.signal as signal
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# <codecell>

def gaussian2D(x, y, sigma):
    return (1.0/(1*math.pi*(sigma**2)))*math.exp(-(1.0/(2*(sigma**2)))*(x**2 + y**2))

# <codecell>

"""make matrix from function"""
def receptiveFieldMatrix(func):
    h = 30
    g = zeros((h,h))
    for xi in range(0,h):
        for yi in range(0,h):
            x = xi-h/2
            y = yi-h/2
            g[xi, yi] = func(x,y);
    return g

# <codecell>

def plotFilter(fun):
    g = receptiveFieldMatrix(fun) 
    plt.imshow(g, cmap=cm.Greys_r)

# <codecell>

plotFilter(lambda x,y:gaussian2D(x,y,4))

# <codecell>

def mexicanHat(x,y,sigma1,sigma2): 
    return gaussian2D(x,y,sigma1) - gaussian2D(x,y,sigma2)

# <codecell>

plotFilter(lambda x,y: mexicanHat(x,y,3,4))

# <codecell>

def oddGabor2D(x,y,sigma,orientation):
    return math.sin(x + orientation*y) * math.exp(-(x**2 + y**2)/(2*sigma))

# <codecell>

def evenGabor2D(x,y, sigma, orientation):
    return math.cos(x + orientation*y) * math.exp(-(x**2 + y**2)/(2*sigma))

# <codecell>

plotFilter(lambda x,y: oddGabor2D(x,y,7,1))

# <codecell>

plotFilter(lambda x,y: evenGabor2D(x,y,7,1))

# <codecell>

def edgeEnergy(x,y,sigma, orientation):
    g1= oddGabor2D(x,y,sigma,orientation)
    g2= evenGabor2D(x,y,sigma,orientation)
    return(g1**2+g2**2)

# <codecell>

plotFilter(lambda x,y:edgeEnergy(x,y,50,0))

# <codecell>

zensurImg=mpimg.imread('zensurGrey.png')
zensurImg = zensurImg[:,:,3]

Img_zensurGaussian = signal.convolve(zensurImg,receptiveFieldMatrix(lambda x,y: gaussian2D(x,y,5)), mode='same')
Img_zensurHat = signal.convolve(zensurImg,receptiveFieldMatrix(lambda x,y:mexicanHat(x,y,3,4)), mode='same')
Img_zensurOddGabor = signal.convolve(zensurImg,receptiveFieldMatrix(lambda x,y: oddGabor2D(x,y,5,1)), mode='same')
Img_zensurEvenGabor = signal.convolve(zensurImg,receptiveFieldMatrix(lambda x,y: evenGabor2D(x,y,5,1)), mode='same')

# <codecell>

imgplot = plt.imshow(zensurImg, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_zensurGaussian, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_zensurHat, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_zensurOddGabor, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_zensurEvenGabor, cmap=cm.Greys_r)

# <codecell>

Img_zensurEdgeEnergy = signal.convolve(zensurImg,receptiveFieldMatrix(lambda x,y: edgeEnergy(x,y,100,1)), mode='same')
imgplot = plt.imshow(Img_zensurEdgeEnergy, cmap=cm.Greys_r)

# <codecell>

img=mpimg.imread('stinkbugGrey.png')
greyImage = img[:,:,0]
def gaussian2DBug(x,y): 
    return gaussian2D(x,y,3)
Img_smooth = signal.convolve(greyImage,receptiveFieldMatrix(gaussian2DBug), mode='same')
def mexicanHatBug(x,y):
    return mexicanHat(x,y,2,3)
Img_hat = signal.convolve(greyImage,receptiveFieldMatrix(mexicanHatBug), mode='same')

# <codecell>

imgplot = plt.imshow(greyImage, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_smooth, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_hat, cmap=cm.Greys_r)

# <codecell>

Img_oddGabor2D = signal.convolve(greyImage,receptiveFieldMatrix(lambda x,y: oddGabor2D(x,y,5,1)), mode='same')
Img_evenGabor2D = signal.convolve(greyImage,receptiveFieldMatrix(lambda x,y: evenGabor2D(x,y,5,1)), mode='same')

# <codecell>

imgplot = plt.imshow(Img_oddGabor2D, cmap=cm.Greys_r)

# <codecell>

imgplot = plt.imshow(Img_evenGabor2D, cmap=cm.Greys_r)

# <codecell>

Img_bugEdgeEnergy = signal.convolve(greyImage,receptiveFieldMatrix(lambda x,y: edgeEnergy(x,y,10,1)), mode='same')
imgplot = plt.imshow(Img_bugEdgeEnergy, cmap=cm.Greys_r)

