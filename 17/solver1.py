#!/usr/bin/env python3


import sys
from tqdm import tqdm
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
#np.set_printoptions(edgeitems=30, linewidth=100000)

xt = [153, 199]
yt = [-114, -75]
sol = []
if len(sys.argv) == 2:
  xt = [20, 30]
  yt = [-10, -5]
  sol = []
  with open(sys.argv[1], 'r') as f:
    for l in f:
      s = l.strip().split(',')
      sol.append([int(s[0]), int(s[1])])


xok = []
xsok = []
yok = []
ymax = []
for x in range(xt[1]+1):
  xn = x
  xs = x
  while xn <= xt[1] and xs > 0:
    if xn >= xt[0] and xn <= xt[1]:
      xok.append(x)
      xsok.append(xs)
      break
    xs = xs - 1
    xn += xs


yimpact = 0
for y in tqdm(range(min(1, np.min(yt)), 1000)):
  yn = y
  ys = y
  ym = y
  while yn >= min(0,np.min(yt)):
    if yn > ym:
      ym = yn
    if yn >= np.min(yt) and yn <= np.max(yt):
      yok.append(y)
      ymax.append(ym)
      yimpact = yn
      break
    ys = ys - 1
    yn += ys
if len(yok) > 0:
  print(f'max y {max(ymax)} at pos {np.argmax(ymax)} impact {yimpact}')
  print(yok[np.argmax(ymax)])

xyok = []
for x in xok:
  for y in yok:
#    if x != 6 or y != 9:
#      continue
#    print(f'{x} {y}')
    yn = y
    ys = y
    xn = x
    xs = x
    while yn >= min(0,np.min(yt)) and xn <= xt[1]:
#     print(f'{xn} x {yn}')
      if yn >= np.min(yt) and yn <= np.max(yt) and xn >= xt[0] and xn <= xt[1]:
        xyok.append([x,y])
        yimpact = yn
        break
      ys = ys - 1
      yn += ys
      xs = max(0, xs - 1)
      xn += xs
print(f'number of solutions (part 2): {len(xyok)}')
print(f'xok {len(xok)}, yok {len(yok)}, {len(xok)*len(yok)}')
print(f'ymax {np.max(ymax)}')
if len(sol) > 0:
  for l in sol:
    if l not in xyok:
      print(f'missing {l}')
