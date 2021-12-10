#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label

inp = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    inp.append(list(l.strip()))

print(inp)

openc = ['(', '<', '{', '[']
closec = [')', '>', '}', ']']
closeindex = {')':0, '>':1, '}':2, ']':3}

costlookup ={')': 3, ']':57, '}':1197, '>':25137}

cost = 0

def found(c, l, cost):
  print(f'list {l}')
  if len(l) == 0:
    return (l, cost)
  assert c in openc
  print(f'start {c}')
  f = l.pop(0)
  while f in openc:
    (l, cost) = found(f, l, cost)
    print(l)
    if l is None or len(l)==0:
      return (l, cost)
    f = l.pop(0)
  # close ok
  print(f'close {f} start {c}')
  if c == openc[closeindex[f]]:
    return (l, cost)
  print(f'illegal {f}')
  assert f in closec
  cost += costlookup[f]
  return (l, cost)



for l in inp:
  f = l.pop(0)
  (l, c) = found (f, l, 0)
  cost += c
  print(cost)

print(cost)
