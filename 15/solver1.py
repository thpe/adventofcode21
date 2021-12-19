#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
np.set_printoptions(edgeitems=30, linewidth=100000)

inp = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    inp.append(list(l.strip()))
inp = np.array(inp, dtype=np.int)

inpl = [inp]
for i in range(8):
  ip = inpl[-1] + 1
 # print(ip[ip>9]=1)
  ip[ip > 9] = 1
  print(ip)
  inpl.append(ip)
of = np.array([[0, 1, 2, 3, 4],
               [1, 2, 3, 4, 5],
               [2, 3, 4, 5, 6],
               [3, 4, 5, 6, 7],
               [4, 4, 5, 7, 8]])

m = np.zeros((inp.shape[0]*5, inp.shape[1]*5))
for x in range(5):
  for y in range(5):
    xs =x * inp.shape[0]
    xe =(x+1) * inp.shape[0]
    ys = y * inp.shape[1]
    ye = (y+1) * inp.shape[1]
    d = inpl[of[x,y]]
    print(inpl[of[x,y]])
#    d = ((d-1) % 9) +1
    m[xs:xe,ys:ye] = d
print(m)
print(m[1::inp.shape[0],1::inp.shape[1]])
inp = m
#5/0

dist = np.ones(inp.shape) * inp.shape[0] * inp.shape[1] + 1
print(inp)

neighb = [(1,0), (0,1), (-1, 0), (0, -1)]


start=(0,0)
end = (inp.shape[0] - 1, inp.shape[1] - 1)
heap = []
heappush(heap, (0, (0,0)))
print(dist)
done = dist == 0



while heap:
  n = heappop(heap)
  if done[n[1]]:
    continue
  done[n[1]] = True
  dist[n[1]] = n[0]
#  print(dist)
  cost = n[0]
  if n[1] == end:
#    print(done)
    break
  for i in neighb:
    ind = tuple(np.array(n[1]) + np.array(i))
    if ind[0] < 0 or ind[1] < 0 or ind[0] >= inp.shape[0] or ind[1] >= inp.shape[1]:
      continue
    if dist[ind] > cost + inp[ind]:
      dist[ind] = cost + inp[ind]
      nn= (cost + inp[ind], ind)
      heappush(heap, nn)
#      print(nn)
print(dist)
print(dist[end])

