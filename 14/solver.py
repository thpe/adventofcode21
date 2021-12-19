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
count= {}
for i in letters:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1

print(count)
out = []
for it in tqdm(range(40)):
  out = []
  for i in range(len(letters) - 1):
    s = letters[i] + letters[i+1]
    out.append(letters[i])
    if s in rules:
      c = rules[s]
      out.append(c)
      if c in count:
        count[c] += 1
      else:
        count[c] = 1
  out.append(letters[-1])
  letters = out
  print(count)

#print(out)
#maxel = max(count)
#print(maxel)
#minel = min()
#print(minel)
#print(out.count(maxel) -out.count(minel))
print(count)
print(max(count.values()) - min(count.values()))
