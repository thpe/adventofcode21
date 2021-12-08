#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd


digits = pd.read_csv(sys.argv[1], sep=' ', header=None)


l=digits.drop(columns=[10])

l = digits.applymap(lambda x: sorted(x))
val = 0
for r in range(len(l.index)):
  n = [None for i in range(10)]
  for c in range(len(l.columns)):
    if len(l.loc[r,c]) == 2:
      n[1] = set(l.loc[r,c])
    if len(l.loc[r,c]) == 4:
      n[4] = set(l.loc[r,c])
    if len(l.loc[r,c]) == 3:
      n[7] = set(l.loc[r,c])
    if len(l.loc[r,c]) == 7:
      n[8] = set(l.loc[r,c])

  l5 = []
  l6 = []

  for c in range(len(l.columns)):
    # case 2, 3, 5
    if len(l.loc[r,c]) == 5:
      l5.append(set(l.loc[r,c]))
    # case 0, 6, 9
    if len(l.loc[r,c]) == 6:
      l6.append(set(l.loc[r,c]))

  delete = []
  for i in range(len(l5)):
    s =l5[i]
    if len(s.difference(n[4]).difference(n[7])) ==1 and len(s.difference(n[7])) == 3:
      print(f'5 = {s}')
      n[5] = s.copy()
      delete.append(i)
    if len(s.difference(n[4]).difference(n[7])) ==1 and len(s.difference(n[7])) == 2:
      print(f'3 = {s}')
      n[3] = s.copy()
      delete.append(i)


  delete.reverse()
  for i in delete:
      l5.pop(i)

  first = None
  if len(l5) > 0:
    first = l5[0]
    n[2] = first
    print(f'2 = {s}')
  for i in range(len(l5)):
    if first != l5[i]:
      print('error')

  nine = n[5].union(n[3])
  six = n[5].union(n[3])

  delete = []
  for i in range(len(l6)):
    s = l6[i]
    if len(nine.difference(s)) == 0:
      print(f'9 = {s}')
      n[9] = s
      delete.append(i)

    elif len(s.difference(n[5])) == 1:
      print(f'6 = {s}')
      n[6] = s
      delete.append(i)

  if len(delete) > 0:
    delete.reverse()
    for i in delete:
      l6.pop(i)
  if len(l6) > 0:
    first = l6[0]
    n[0] = first
    print(f'0 = {s}')
  for i in range(len(l6)):
    if first != l6[i]:
      print('error')

  lval = []
  for c in [11, 12, 13, 14]:
      dig = set(l.loc[r,c])
      print(f'searching {dig}')
      for i in range(len(n)):
        if dig == n[i]:
          lval.append(i)
  lval = lval[0] * 1000 + lval[1] * 100 + lval[2] * 10 + lval[3]
  print(lval)
  val += lval

print(f'solution {val}')
