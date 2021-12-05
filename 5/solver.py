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

chart = np.zeros((xmax, ymax))
fail = 0
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
  if l[1] == l[3]:
    mi = np.min([l[0], l[2]])
    ma = np.max([l[0], l[2]])
    chart[mi:ma+1,l[1]] += 1
    count = np.abs(l[0] - l[2]) + 1
    if l[0] > l[2]:
      fail +=1
  else:
    print('============fail=============')
    print(l)
  print(count)
  print(np.sum(chart))
print(fail)
danger = chart > 1
print(np.sum(danger))
