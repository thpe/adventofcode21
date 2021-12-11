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
octo = np.array(inp, dtype=int)
print(octo)

assert 0 == np.sum(octo==9)

off = [[-1, -1], [-1, 0], [-1, 1],
       [0, -1],  [0, 1],
       [1, -1], [1, 0], [1, 1]]


mask = np.zeros(octo.shape)
mask = mask ==1
print(mask)

def light(arr, x, y, c, mask):
  if mask[x, y]:
    return (arr, c, mask)
  mask[x, y] = True
  c = c + 1
  print((x,y))
  print(mask)
  print(np.ma.array(arr, mask=mask))

  for o in off:
    li = np.array([x,y]) + o
    print(li)
    if (li < 0).any():
      continue
    if li[0] >= arr.shape[0] or li[1] >= arr.shape[1]:
      continue
    if arr[li[0], li[1]] < 9 and not mask[li[0], li[1]]:
      arr[li[0], li[1]] += 1
    if arr[li[0], li[1]] >= 9:
      (arr, c, mask) = light(arr, li[0], li[1], c, mask)
  arr[x,y] = 0
  assert 0 == np.sum(arr >=10)
  return (arr, c, mask)

count = 0
for step in range(10000):
  mask = np.zeros(octo.shape)
  mask = mask ==1
  ind = np.argwhere(octo == 9)
  for i in ind:
    (octo, count, mask) = light(octo, i[0], i[1], count, mask)
  assert 0 == np.sum(octo==9)

  print(ind)
  ind = np.argwhere(mask == False)
  for i in ind:
    octo[i[0], i[1]] += 1
  print(octo)
  if (octo == 0).all():
    count = step
    break

print(count + 1)
