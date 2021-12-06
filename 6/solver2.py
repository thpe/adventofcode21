#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd


fish = pd.read_csv(sys.argv[1], header=None, squeeze = True)
#fish = fish.transpose()
print(fish)

fishbirth = np.zeros((1, 7))
for c in range(len(fish.columns)):
  f = fish.iloc[0, c]
  print(f)
  fishbirth[0, f] += 1
print(fishbirth)
fishbirth = np.repeat(fishbirth, repeats=300, axis=0)

print(fishbirth)

for i in range(int(sys.argv[2])):
  dow = i % 7
  #print(f'day {i}')
  #print(fishbirth[i])
  nextdow = (dow + 2) % 7
  cur = fishbirth[i, dow]
  if cur > 0:
    fishbirth[i+3:,nextdow] += cur
  print(f'day {i} fish {np.sum(fishbirth[i+5])} born {cur}')
  #print(fishbirth[i+2])
