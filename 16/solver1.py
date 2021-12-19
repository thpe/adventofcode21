#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
np.set_printoptions(edgeitems=30, linewidth=100000)

inp = []
with open(sys.argv[1], 'r') as f:
  for l in f:
    inp.append(list(l.strip()))

lookup=[]
for i in range(16):
  lookup.append([(i >> (x))&1 for x in reversed(range(4))])

print (lookup)
b=[]
for l in range(len(inp)):
  for x in range(len(inp[l])):
    b = b + lookup[int(inp[l][x], 16) ]

print (b)

versions = []
typs = []
state = 0
substate = 0
version = 0
length = []
typ = 0
i = 0
N = len(b)

op = {0: 'sum',
      1: 'product',
      2: 'minimum',
      3: 'maximum',
      5: 'greater than',
      6: 'less than',
      7: 'equal to'}

opop = {0: np.sum,
        1: np.product,
        2: np.min,
        3: np.max,
        5: lambda x: 1 if x[0] >  x[1] else 0,
        6: lambda x: 1 if x[0] <  x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0}

while i < len(b):
    bit = b[i]
    print(f'bit {i}')
    if state == 0:
      if len(length) > 0:
        print(f'    op {length[-1]}')
      if i > N - 3:
        print('not enough bits')
        break
      version = np.sum([b[i + x] << (2 - x) for x in range(3)])
      state = 1
      substate = 0
      versions.append(version)
      print(f'version {version}')
      print(f'  {b[i:i+3]}')
      version = 0
      i += 2
    elif state == 1:
      if i > N - 3:
        print('not enough bits')
        break
      print(f'  {b[i:i+3]}')
      typ = np.sum([b[i + x] << (2 - x) for x in range(3)])
      state = 4 if typ == 4 else 3
      substate = 0
      print(f'  type {typ} op {typ != 4} state {state}')
      typs.append(typ)
      i += 2
    elif state == 3:
      if bit == 0:
        #15 bit
        state = 15
        print(f'  15 bit')
      else:
        # 11bit
        state= 11
        print(f'  11 bit')
    elif state == 4:
      io = i
      # value
      if i > N - 4:
        print(f'not enough bits {i} {N}')
        break
      else:
        v = 0
        while b[i] != 0:
          v = v << 4
          print(f'    read {b[i:i+6]}')
          i = i + 1
          v += np.sum([b[i + x] << (3 - x) for x in range(4)])
          i += 4
        print(f'    read {b[i:i+6]} done')
        v = v << 4
        i = i + 1
        v += np.sum([b[i + x] << (3 - x) for x in range(4)])
        i += 3
        print(f'    value = {v}')
        length.append(['v', i - io + 1, v, None])
        state = 0

    elif state == 11:
      # length in packets
      if i > N - 11:
        print('not enough bits')
        break
      print(f'  {b[i:i+11]}')
      l = np.sum([b[i + x] << (10 - x) for x in range(11)])
      print (f'    p length {l}')
      length.append(['p',12, typ, l])
      substate = 0
      state = 0
      i += 10
    elif state == 15:
      # length in bits
      if i > N - 15:
        print('not enough bits')
        break
      l = np.sum([b[i + x] << (14 - x) for x in range(15)])
      print (f'    b length {l}')
      length.append(['b', 16, typ, l])
      substate = 0
      state = 0
      i += 14
    else:
      print ('unknown state')
      break
    i += 1

print(length)
print(versions)
print(f'solution 1: {np.sum(versions)}')



def calc(oper):
  if oper[0][0] == 'v':
    return (oper[0][2], oper[1:], oper[0][1]+6)
  elif oper[0][0] == 'p':
    lop = oper.pop(0)
    l = lop[3]
    t = lop[2]
    b = lop[1]
    values = []
    count = b + 6
    print(f'count {count}')
    for i in range(l):
      (v, oper, c) = calc(oper)
      count += c
      values.append(v)
      print(f'count {count}')
    return (opop[t](values), oper, count)
  elif oper[0][0] == 'b':
    lop = oper.pop(0)
    l = lop[3]
    t = lop[2]
    b = lop[1]
    values = []
    count = 0
    while count < l:
      (v, oper, c) = calc(oper)
      count += c
      values.append(v)
    count += b + 6
    return (opop[t](values), oper, count)

res = calc(length)
print(f'solution 2: {res}')
print(f'bytes: {len(b)}')

