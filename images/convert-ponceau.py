import mahotas
from scipy import ndimage
import numpy as np
import pylab

im = mahotas.imread('exosomes-vs-whole.JPG')

for i in range(3):
	# Process each band separately
	level = im[:,:,i]
	# This produces a VERY blurry image - any small features are lost leaving just large changes in color
	levelg = ndimage.gaussian_filter(level, 64)
	# Use the median of the blurred image to correct the background across the image
	med = np.median(levelg.flatten())
	im[:,:,i] = level - (levelg - med)

# For this image the best contrast between foreground and background was achieved by looking at just bands 1 & 2
im12 = (im[:,:,1] + im[:,:,2]) / 2

# Display the image
pylab.imshow(im12)
pylab.gray()
pylab.show()