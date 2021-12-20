#!/usr/bin/env python3


import sys
from tqdm import tqdm
import re
from math import floor, ceil
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
np.set_printoptions(edgeitems=200, linewidth=100000)
from numpy import rot90, array
import matplotlib.pyplot as plt



alg = []
image = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    row = [x == '#' for x in list(l.strip())]
    image.append(row)

with open(sys.argv[2], 'r') as f:
  for l in f:
    alg = [x == '#' for x in list(l.strip())]
    break

image = np.array(image)
alg=np.array(alg)
print(image*1)
print(image.shape)
print(alg*1)
print(alg.shape)


def index(a, p=False):
  pot = 2 ** np.arange(len(a) - 1, -1, -1)
  idx = np.sum(pot*a)
  if p:
    print(f'{np.array(a)*1} {pot*a} {idx}')
  return idx

img = np.zeros((image.shape[0]*3,image.shape[1]*3))
print(img.shape)
img = img == 1
xbd = [image.shape[0]*1, 2 * image.shape[0]]
ybd = [image.shape[1]*1, 2 * image.shape[1]]
img[xbd[0]:xbd[1],ybd[0]:ybd[1]] = image

res = np.zeros(img.shape)
res = res == 1
print(img[xbd[0]:xbd[1],ybd[0]:ybd[1]]*1)
print('be patient, this takes a while')
for it in np.arange(1,51):
  ad = np.array([-6, 6])

#  xbd += ad
#  ybd += ad
  xbd = [0, img.shape[0]]
  ybd = [0, img.shape[1]]


  for x in range(xbd[0], xbd[1]):
    for y in range(ybd[0], ybd[1]):
      val = []
      for xoff in [-1, 0, 1]:
        for yoff in [-1, 0, 1]:
          xidx = x+xoff
          # we intentionally wrap around to simulate an infinite image
          if xidx >= img.shape[0]:
            xidx = -1
          yidx = y+yoff
          if yidx >= img.shape[1]:
            yidx = -1
      #    print(f'{xoff}, {yoff}')
      #    print(f'{x+xoff}, {y+yoff}')
          val.append(img[xidx, yidx])
      #if x == 12:
      #  al = alg[index(val, True)]
      #  print(f'{x} {y} {al}')
      #else:
      al = alg[index(val)]
      res[x, y] = al
  img= np.copy(res)
  res = np.zeros(img.shape)
  res = res == 1
  print(f'{it} count {np.sum(img)}')
  #print(img[xbd[0]:xbd[1],ybd[0]:ybd[1]]*1)


#print(img[xbd[0]-10:xbd[1]+10,ybd[0]-10:ybd[1]+10]*1)
#print(img*1)
print(f'solution {np.sum(img)}')
