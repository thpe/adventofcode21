#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label

inp = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    inp.append(list(l.strip()))
inp = np.array(inp, dtype=np.int)

mask = inp < 9
larr, num_feature = label(mask)
num_feature +=1
mindeep = np.ones(num_feature)
size = np.zeros(num_feature)

for i in range(num_feature):
  chart = np.ma.array(inp, mask=~(larr==i))
  m = np.min(chart)
  if m == 9:
    continue
  mchart = np.ma.array(inp, mask=(larr!=i) | (inp !=m) )
  if mchart.count() ==1:
    size[i] = chart.count()

size = np.sort(size)
res = size[-3] * size[-2] * size[-1]

print(res)
