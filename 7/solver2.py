#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd
from scipy.special import comb

np.set_printoptions(edgeitems=30, linewidth=100000)
position = pd.read_csv(sys.argv[1], header=None)

position = np.array(position)
mx =np.max(position)
#print(position)
#print(f'max {mx}')


x = np.linspace(1, mx+1, mx+1)
d = comb(x, 2)
dr = d[::-1]

cost = np.zeros(mx+1, dtype=np.float)

for p in range(position.shape[1]):
  p = position[0,p]
  if p > 0 and p < mx:
    cost[0:p] += dr[-p-1:-1]
    cost[p:] += d[:mx+1-p]
  elif p == 0:
    cost += d
  elif p == mx:
    cost += dr

print(cost)
print(f'pos {np.argmin(cost)} cost {np.min(cost)}')
