#!/usr/bin/env python3


import copy
import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label

np.set_printoptions(edgeitems=30, linewidth=100000)
cave = pd.read_csv(sys.argv[1], sep=',', header=None)
cave = np.array(cave, dtype=int)
x = int(np.max(cave[:,0]))
y = int(np.max(cave[:,1]))
print(f'{x} x {y}')

my = re.compile(r'fold along y=(\d+)')
mx = re.compile(r'fold along x=(\d+)')

folds = []

with open(sys.argv[2], 'r') as f:
  for l in f:
    res = my.match(l)
    if res:
      folds.append((0, res.group(1)))
    res = mx.match(l)
    if res:
      folds.append((1, res.group(1)))
m = np.zeros((y+1, x+1))
for i in range(cave.shape[0]):
  m[cave[i, 1], cave[i, 0]] += 1

def apply_fold(f, mat):
    up = mat[:f,:]
    do = mat[f+1:,:]
    do = do[::-1,:]
    nu = None
    if up.shape[0] > do.shape[0]:
      ny = up
      ny[ny.shape[0] - do.shape[0]:,:] += do
    else:
      ny = do
      ny[ny.shape[0] - up.shape[0]:,:] += up
    print(f'number of points {np.sum(ny!=0)}')
    mat = ny
    return mat

for fold in folds:
  f = int(fold[1])
  print(f'fold at {f} with axis {fold[0]}')
  if fold[0] == 0:
    m = apply_fold(f, m)
  else:
    m = np.transpose(apply_fold(f, np.transpose(m)))



m[m!=0] = 11
print(np.ma.array(m, mask=m== 0, dtype=int))
