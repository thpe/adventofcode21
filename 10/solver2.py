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
openindex = {'':0, '>':1, '}':2, ']':3}

costlookup ={')': 1, ']':2, '}':3, '>':4}
ocostlookup ={'(': 1, '[':2, '{':3, '<':4}

cost = 0

def found(c, l, cost):
  if cost == -1:
    return (l, cost)
  print(f'list {l}')
  if len(l) == 0:
    print(f'old cost{cost} start {c} {ocostlookup[c]}')
    cost = 5 * cost + ocostlookup[c]
    print(f'new cost{cost} start {c}')
    return (l, cost)
  assert c in openc
  print(f'start {c}')
  f = l.pop(0)
  while f in openc:
    (l, cost) = found(f, l, cost)
    if cost == -1:
      return (l, cost)
    print(l)
    if l is None or len(l)==0:
      print(f'old cost{cost} start {c} {ocostlookup[c]}')
      cost = 5 * cost + ocostlookup[c]
      print(f'new cost{cost} start {c}')
      return (l, cost)
    f = l.pop(0)
  # close ok
  print(f'close {f} start {c}')
  if c == openc[closeindex[f]]:
    return (l, cost)
  print(f'illegal {f}')
  assert f in closec
  return (l, -1)


costlist = []
for l in inp:
  f = l.pop(0)
  c = 0
  while f in openc:
    (l, c) = found(f, l, c)
    if c == -1:
      break
    print(l)
    if l is None or len(l)==0:
      break
    f = l.pop(0)
  print(f'+++++++++++++++++++++++++++++++final {c}')
  if c != -1:
    costlist.append(c)
  else:
    print("+++++++++++++++++DROPED++++++++++++++")

print(costlist)
print(len(costlist))
print(np.median(costlist))
