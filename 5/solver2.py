#!/usr/bin/env python3


import sys
import re
import numpy as np

reline = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

y = 0
x = 0

data = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    m = reline.match(l)
    if m:
      data.append([int(m.group(1)),
                   int(m.group(2)),
                   int(m.group(3)),
                   int(m.group(4))])


a = np.array(data)
print(a)
m = np.max(a, axis=0)
print(m)
xmax = np.max([m[0], m[2]])
ymax = np.max([m[1], m[3]])

chart = np.zeros((xmax+1, ymax+1))
fail = 0
acount = 0
for i in range (a.shape[0]):
  l = a[i]
  count = 0
  if l[0] == l[2]:
    mi = np.min([l[1], l[3]])
    ma = np.max([l[1], l[3]])
    chart[l[0],mi:ma+1] += 1
    count = np.abs(l[1] - l[3]) + 1
    if l[1] > l[3]:
      fail +=1
  elif l[1] == l[3]:
    mi = np.min([l[0], l[2]])
    ma = np.max([l[0], l[2]])
    chart[mi:ma+1,l[1]] += 1
    count = np.abs(l[0] - l[2]) + 1
    if l[0] > l[2]:
      fail +=1
  else:
    minx = l[0]
    miny = l[1]
    maxx = l[2]
    maxy = l[3]
    if minx > maxx:
      minx = l[2]
      miny = l[3]
      maxx = l[0]
      maxy = l[1]
    ix = np.arange(minx, maxx + 1)
    iy = np.arange(miny, maxy + 1)
    if miny > maxy:
      iy = np.arange(miny, maxy - 1, -1)
    for (x,y) in zip(ix, iy):
      chart[x,y] +=1
    count = len(ix)
    print(f'===diag=== {l[0]} {l[1]} {l[2]} {l[3]}==')
    print(f'===diag=== {minx} {miny} {maxx} {maxy}==')
    print(ix)
    print(iy)
  print(f'count {count}')
  acount += count
  print(f'acount {acount}')
  print(np.sum(chart))
  assert acount == np.sum(chart)
print(fail)
danger = chart > 1
print(np.sum(danger))
