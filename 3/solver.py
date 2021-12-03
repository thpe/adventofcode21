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

inp = np.array(inp)
N = inp.shape[0]
s = np.sum(inp, axis=0)
print(s)
res = s > (N / 2.0)
print(res)
print(~res)
M = res.shape[0]

mul = np.arange(M - 1, -1, -1)
mul = np.power(2, mul)
gamma = np.ma.array(mul, mask=res)
eps = np.ma.array(mul, mask=~res)
print(mul)
print(gamma.sum())
print(eps.sum())
print(gamma.sum() * eps.sum())
