import mahotas
import numpy as np
from PIL import Image


#
# Conversion back and forth between PIL images and mahotas/numpy images
#
# Assumes grayscale images
#

def vision2image(im):
    """Convert a mahotas loaded image into one compatible with PIL"""
    m, n = np.shape(im)
    imout = Image.new('L', (n,m))
    pix = imout.load()
    for x in range(m):
        for y in range(n):
            #pix[y,x] = 255 - im[x,y]
            if im[x,y] > 0:
                pix[y,x] = 0
            else:
                pix[y,x] = 255
    return imout

def image2vision(im):
    """Convert a PIL loaded image into one compatible with mahotas"""
    m, n = im.size
    imout = np.empty((n,m), dtype=np.uint8)
    pix = im.load()
    for x in range(m):
        for y in range(n):
            imout[y,x] = pix[x,y]
    return imout
