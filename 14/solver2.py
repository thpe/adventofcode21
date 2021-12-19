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

def dfs(node, count, depth):
  if depth == 0:
    return count
  n0 = node[0]
  n1 = node[1]
  m = None
  if node in rules:
    m = rules[node]

    if m in count:
      count[m] += 1
    else:
      count[m] =1
    count = dfs(n0+m, count, depth-1)
    count = dfs(m+n1, count, depth-1)
  return count

out = []
for i in tqdm(range(len(letters) - 1)):
  s = letters[i] + letters[i+1]
  count = dfs(s, count, 40)
print(count)

#print(out)
#maxel = max(count)
#print(maxel)
#minel = min()
#print(minel)
#print(out.count(maxel) -out.count(minel))
print(count)
print(max(count.values()) - min(count.values()))
