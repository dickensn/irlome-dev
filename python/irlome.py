#!/usr/bin/env python3
''' IRLOME class
Dev script for better image analysis
'''

__author__ = "Nick Dickens"
__copyright__ = "Copyright 2018, Nicholas J. Dickens"
__email__ = "dickensn@fau.edu"
__license__ = "MIT"

import sys

import matplotlib.pyplot as plt

from skimage import io
from skimage import exposure
from skimage import util

from skimage.color import rgb2hed
from matplotlib.colors import LinearSegmentedColormap

# Create an artificial colour maps
cmap_reds = LinearSegmentedColormap.from_list('mycmap', ['white', 'red'])
cmap_greens = LinearSegmentedColormap.from_list('mycmap', ['white','green'])
cmap_blues = LinearSegmentedColormap.from_list('mycmap', ['white','blue'])

filename = sys.argv[1]
image_rgb = io.imread(filename)
#image_norm = exposure.equalize_hist(image_rgb)
#image_hed = rgb2hed(image_rgb)



fig, axes = plt.subplots(2, 2, figsize=(7, 6), sharex=True, sharey=True)
ax = axes.ravel()

channel0 = image_rgb[:, :, 0]
channel1 = image_rgb[:, :, 1]
channel2 = image_rgb[:, :, 2]

#chlorophyl A absorbs most at 420nm rgb()
#chlorophyll B absorbs most at 460nm rgb(0,123, 255)
#600nm rgb(255,190, 0)
#500nm rgb(0,255, 146)
#550 rgb(163,255, 0)

# if rgb > chlorophyl B set to white
#image_rgb[image_rgb[:, :, 0] > 0 and image_rgb[:, :, 1] > 122 and image_rgb[:, :, 3] > 254] = 0

#look for what is missing, rather than what is present

def mask_by_color(rgb_data, rgb):
    '''returns an image where pixels at this rgb are
    '''
    red_true = rgb_data[:, :, 0] == rgb[0]
    green_true = rgb_data[:, :, 1] == rgb[1]
    blue_true = rgb_data[:, :, 2] == rgb[2]

    #set everything to black
    rgb_data[:,:] = [0,0,0]
    #set all true to white
    all_true = rgb_data.all(red_true and green_true and blue_true)
    rgb_data[all_true] = [255, 255, 255]
    return rgb_data

ax[0].imshow(image_rgb)
ax[0].set_title("Original Image")

image_rgb = util.invert(image_rgb)
ax[1].imshow(image_rgb) #, cmap=cmap_reds
ax[1].set_title("Inverted")

ax[2].imshow(mask_by_color(image_rgb, [0, 123, 255])) #, cmap=cmap_reds
ax[2].set_title("Queried")

ax[3].imshow(exposure.equalize_hist(image_rgb[:, :, 2]), cmap=cmap_blues)
ax[3].set_title("Blues")



for a in ax.ravel():
    a.axis('off')

fig.tight_layout()
fig.savefig('new.png')
