#!/usr/bin/env python3
''' IRLOME maps
'''

__author__ = "Nick Dickens"
__copyright__ = "Copyright 2018, Nicholas J. Dickens"
__email__ = "dickensn@fau.edu"
__license__ = "MIT"

import matplotlib.pyplot as plt
import mplleaflet

points = []
with open("../web/data/user_data.csv") as in_fh:
  for line in in_fh:
    line = line.rstrip()
    lon, lat, color = line.split(",")
    points.append((lon, lat, color))



for point in points:
    plt.plot(point[0],point[1],'s',color=point[2])

mplleaflet.show(path="../web/map.html")
