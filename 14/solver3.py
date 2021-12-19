#!/usr/bin/env python3


import copy
import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from tqdm import tqdm


rule = re.compile(r'(..) -> (.)')

rules = {}

letters = []

tuples = {}
with open(sys.argv[1], 'r') as f:
  for l in f:
    letters = list(l.strip())

with open(sys.argv[2], 'r') as f:
  for l in f:
    res = rule.match(l)
    if res:
      rules[res.group(1)] = res.group(2)


print (letters)
print(rules)


for i in range(len(letters)-1):
  t = letters[i] + letters[i+1]
  print(t)
  if t in tuples:
    tuples[t] += 1
  else:
    tuples[t] = 1
#copy.deepcopy(tuples)

for r in range(40):
  ntuples = {}
  for k, v in tuples.items():
    print (k, v)
    if k in rules:
      t = rules[k]
      nt = k[0] + t
      if nt in ntuples:
        ntuples[nt] += v
      else:
        ntuples[nt] = v
      nt = t + k[1]
      if nt in ntuples:
        ntuples[nt] += v
      else:
        ntuples[nt] = v
  tuples = ntuples
  print(tuples)


count = {}

for k, v in tuples.items():
    if k[1] in count:
      count[k[1]] += v
    else:
      count[k[1]] = v
count[letters[0]] += 1
print(count)

print(max(count.values()) - min(count.values()))

