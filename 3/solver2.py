#!/usr/bin/env python3


import sys
import re
import numpy as np

inp = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    l = l.strip()
    row = []
    for i in range(len(l)):
      row.append(int(l[i]))
    inp.append(row)

ina = np.array(inp)
N = ina.shape[0]
NH = N / 2.0
M = ina.shape[1]
pos = np.ma.array(inp)
count = N
for i in range(M):
  s = pos.sum(axis=0)
  c = 1
  if s[i] >= count / 2.0:
    c = 0

  mask = pos[:,i] == c
  mask = mask.reshape(N, 1)
  mask = np.repeat(mask, repeats=M, axis=1)
  pos.mask = pos.mask | mask
  print(pos.mask)

  count = np.sum(~pos.mask[:,0])
  if count == 1:
    break
n = np.argmax((~pos.mask[:,0]).flatten())
print(n)
print(pos)
res = pos[n]

mul = np.arange(M - 1, -1, -1)
mul = np.power(2, mul)
O2 = np.ma.array(mul, mask=res==0)
print(O2)
O2 = np.sum(O2)
print(O2)
pos = np.ma.array(inp)
count = N
for i in range(M):
  s = pos.sum(axis=0)
  c = 1
  if s[i] < count / 2.0:
    c = 0

  mask = pos[:,i] == c
  mask = mask.reshape(N, 1)
  mask = np.repeat(mask, repeats=M, axis=1)
  pos.mask = pos.mask | mask
  print(pos.mask)

  count = np.sum(~pos.mask[:,0])
  if count == 1:
    break
n = np.argmax((~pos.mask[:,0]).flatten())
print(n)
print(pos)
res = pos[n]

mul = np.arange(M - 1, -1, -1)
mul = np.power(2, mul)
CO2 = np.ma.array(mul, mask=res==0)
print(CO2)
CO2 = np.sum(CO2)
print(CO2)
print(CO2 * O2)
