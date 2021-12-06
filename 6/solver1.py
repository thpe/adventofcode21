#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd


fish = pd.read_csv(sys.argv[1], header=None, squeeze = True)
fish = fish.transpose()
print(fish)
for i in range(18):
  parentidx = np.array(fish) == 0
  born = (parentidx).sum()
  fish = fish - 1
  if born > 0:
    fish[parentidx] = 6
    newfish = pd.Series(np.ones((born)) * 8)
#    print(newfish)
    fish = pd.concat([fish, newfish], ignore_index=True)
  print(f'day {i} fish {len(fish.index)} born {born}')
#  print(fish)


#print(fish)
