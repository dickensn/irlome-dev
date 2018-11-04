#!/usr/bin/env python3
''' IRLOME class
'''

__author__ = "Nick Dickens"
__copyright__ = "Copyright 2018, Nicholas J. Dickens"
__email__ = "dickensn@fau.edu"
__license__ = "MIT"

import sys
import random

import numpy as np
from PIL import Image


class Cluster:
    def __init__(self):
        self.pixels = []
        self.centroid = None

    def add_pixel(self, pixel):
        self.pixels.append(pixel)

    def set_centroid(self):
        R = [colour[0] for colour in self.pixels]
        G = [colour[1] for colour in self.pixels]
        B = [colour[2] for colour in self.pixels]

        R = int(sum(R) / len(R))
        G = int(sum(G) / len(G))
        B = int(sum(B) / len(B))

        self.centroid = (R, G, B)
        self.pixels = []

        return self.centroid


class Kmeans:
    def __init__(self, k=3, max_iter=5, min_distance=5.0, sample_size=300):
        self.k = k
        self.max_iter = max_iter
        self.min_distance = min_distance
        self.sample_size = (sample_size, sample_size)

    def run(self, image):
        self.image = image
        self.image.thumbnail(self.sample_size)
        self.pixels = np.array(image.getdata(), dtype=np.uint8)

        self.clusters = [None for i in range(self.k)]
        self.previous_clusters = None

        #print(self.pixels.shape)
        randomPixels = random.sample(list(self.pixels[:]), self.k)

        # print(randomPixels)


        for idx in range(self.k):
            self.clusters[idx] = Cluster()
            self.clusters[idx].centroid = randomPixels[idx]

        iterations = 0

        while self.shouldExit(iterations) is False:

            self.previous_clusters = [cluster.centroid for cluster in self.clusters]

            #print(iterations)

            for pixel in self.pixels:
                self.assignClusters(pixel)

            for cluster in self.clusters:
                cluster.set_centroid()

            iterations += 1

        return [cluster.centroid for cluster in self.clusters]

    def assignClusters(self, pixel):
        shortest = float('Inf')
        for cluster in self.clusters:
            distance = self.calcDistance(cluster.centroid, pixel)
            if distance < shortest:
                shortest = distance
                nearest = cluster

        nearest.add_pixel(pixel)

    def calcDistance(self, a, b):

        result = np.sqrt(sum((a - b) ** 2))
        return result

    def shouldExit(self, iterations):

        if self.previous_clusters is None:
            return False

        for idx in range(self.k):
            dist = self.calcDistance(
                np.array(self.clusters[idx].centroid),
                np.array(self.previous_clusters[idx])
            )
            if dist < self.min_distance:
                return True

        if iterations <= self.max_iter:
            return False

        return True

    def get_colors(self):
        list_of_colors = []
        for cluster in self.clusters:
            list_of_colors.append(cluster.centroid)
        return list_of_colors
    # ############################################
    # The remaining methods are used for debugging
    def showImage(self):
        self.image.show()

    def showCentroidColours(self):
        for cluster in self.clusters:
            image = Image.new("RGB", (200, 200), cluster.centroid)
            image.show()

    def showClustering(self):
        localPixels = [None] * len(self.image.getdata())
        for idx, pixel in enumerate(self.pixels):
                shortest = float('Inf')
                for cluster in self.clusters:
                    distance = self.calcDistance(
                        cluster.centroid,
                        pixel
                    )
                    if distance < shortest:
                        shortest = distance
                        nearest = cluster

                localPixels[idx] = nearest.centroid

        w, h = self.image.size
        localPixels = np.asarray(localPixels)\
            .astype('uint8')\
            .reshape((h, w, 3))

        colourMap = Image.fromarray(localPixels)
        colourMap.show()

if __name__=="__main__":
    kmeans = Kmeans(k=5)
    image =  Image.open(sys.argv[1])
    kmeans.run(image)
    #kmeans.showClustering()
    print(kmeans.get_colors())
