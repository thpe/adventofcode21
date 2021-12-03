#!/usr/bin/env python3


import sys
import pandas as pd
import numpy as np

last = -1
count = 0
a = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    a.append(int(l))

a = np.array(a)
last = -1
count = 0
for i in range(a.shape[0] - 2):
    s = a[i] + a[i+1] + a[i+2]
    if last != -1 and last < s:
        count += 1
    last = s
    print (s)



print(count)
