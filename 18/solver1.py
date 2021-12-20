#!/usr/bin/env python3


import sys
from tqdm import tqdm
import re
from math import floor, ceil
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
#np.set_printoptions(edgeitems=30, linewidth=100000)

def add(l1, l2):
  print(l1)
  print(l2)
  l = l1+ l2
  for i in l:
    i[1] += 1
  return l

def split(l):
  print(f'spl {l}')
  for i in range(len(l)):
    if l[i][0] > 9:
#      if i > 0:
        left = floor(l[i][0] / 2)
        right = ceil(l[i][0] / 2)
        l[i][0] = right
        l[i][1] += 1
        l.insert(i, [left, l[i][1]])
        print(f'->  {l}')
        return l
  return None

def mag(l):
  while len(l) > 1:
#    print(l)
    m = 0
    mv = 0
    for i in l:
      if i[1] > mv:
        mv = i[1]
#    print(f'max {mv}')
    for i in reversed(range(len(l))):
      if l[i][1] == mv:
        res = l[i][0] * 2 + l[i-1][0] * 3
        l[i-1][0] = res
        l[i-1][1] -= 1
        l.pop(i)
  return l

def explode(l):
  print(f'exp {l}')
  for i in range(len(l)):
    if l[i][1] > 4:
      print(l[i:i+1])
      if i > 0:
        l[i-1][0] += l[i][0]
      if i < len(l) - 2:
        assert l[i+1][1] == 5
        l[i+2][0] += l[i+1][0]
      l.pop(i+1)
      l[i][0] = 0
      l[i][1] = l[i][1] - 1
      print(f'->  {l}')
      return l
  return None
def red(l):
  changed = True
  while changed:
    changed = False
    while True:
      res = explode(l)
      if res is not None:
        changed = True
        l = res
        continue
      else:
        break
    res = split(l)
    if res is not None:
      changed = True
      l = res
      continue
  return l
numbers = []
number = []
level = 0
left = True
with open(sys.argv[1], 'r') as f:
  for l in f:
    ll = list(l.strip())
    for c in ll:
      if c == '[':
        level+=1
      elif c == ']':
        level-=1
      elif c == ',':
        left = not left
      else:
        number.append([int(c), level])
    numbers.append(number)
    number = []
print(numbers)



res = numbers[0]
for i in range(1, len(numbers)):
  res = red(add(res, numbers[i]))
print(res)
print(mag(res))
