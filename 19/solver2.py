#!/usr/bin/env python3


import sys
from tqdm import tqdm
import re
from math import floor, ceil
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label
from heapq import heappush, heappop
#np.set_printoptions(edgeitems=30, linewidth=100000)
from numpy import rot90, array


rs = re.compile(r'-+ scanner (\d+) -+')
rc = re.compile(r'(-?\d+),(-?\d+),(-?\d+)')
#rc = re.compile(r'(-?\d+),(-?\d+),(-?\d+)')

scanner = []
beacons = []

with open(sys.argv[1], 'r') as f:
  for l in f:
    res = rs.match(l)
    if res:
      scanner.append([])
    res = rc.match(l)
    if res:
      scanner[-1].append([int(res.group(x)) for x in [1,2,3]])
scanner = [np.array(b) for b in scanner]
print(scanner)
print(len(scanner))
rollmat = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=np.float)
turnmat = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=np.float)

# thank you stack exchange :-)
def get_24_rotation():
    rotations = []
    current_rot = np.eye(3)
    for cycle in range(2):
        for step in range(3): # RTTT 3 times
            current_rot = rollmat @ current_rot
            rotations.append(current_rot) # R
            for i in range(3): # TTT
                current_rot = turnmat @ current_rot
                rotations.append(current_rot)
        current_rot = rollmat @ turnmat @ rollmat @ current_rot # RTR
    return rotations

f = 0
todo = [[i + 1, np.zeros(3), np.identity(3)] for i in range(len(scanner[1:]))]
doing = [[0, np.zeros(3), np.identity(3)]]
doingn = []
done = []
print('match')
print(f'{len(todo)} {len(doing)} {len(done)}')
assert len(todo)+len(doingn)+len(doing)+len(done) == len(scanner),f'{len(todo)} {len(doingn)} {len(doing)} {len(done)}'
#print(scanner[0])

# while we have something to do
while len(doing) > 0:
  # select a scanner with known position and rotation
  for f in doing:
    # select a scanner without position
    for toidx in reversed(range(len(todo))):
      to = todo[toidx]
      # try all rotations
      for r in get_24_rotation():
        d = {}
        # try all 'from' beacons
        for beacon in range(scanner[f[0]].shape[0]):
            targets = scanner[to[0]]
            # try all 'to' beacons
            for y in range(targets.shape[0]):
              # use the known rotation on the 'from' beacon
              fBeacon = np.matmul(scanner[f[0]][beacon], f[2])
              # use the rotation to test on the 'to' beacon
              tBeacon = np.matmul(targets[y], r)
              # estimate 'to' scanner position
              t_pos = fBeacon - tBeacon
              assert t_pos.shape == (3,), t_pos.shape
              v = str(int(t_pos[0])) + ',' + str(int(t_pos[1])) + ',' + str(int(t_pos[2]))
              # add to dictionary for counting
              if v in d:
                d[v] += 1
              else:
                d[v] = 1

        #print(d)
        m = max(d.values())
        # if we found 12 common beacons, we can fix the position of this node
        if m >= 12:
          k = max(d, key=d.get)
          kv = k.split(',')
          kv = [int (val) for val in kv]
#          print(f'{f} - {to}: {k} -> {m}')
          doingn.append(todo.pop(toidx))
          # add 'from' position to get absolute position
          doingn[-1][1] = np.array(kv) + f[1]
          doingn[-1][2] = r
          break



    done.append(f)
  doing = doingn
  doingn = []
  print(f'{len(todo)} {len(doing)} {len(done)}')
  assert len(todo)+len(doingn)+len(doing)+len(done) == len(scanner),f'{len(todo)} {len(doingn)} {len(doing)} {len(done)}'

d = 0
for i in range(len(done)):
  for j in range(len(done)):
    d = max(d, np.sum(np.abs(done[i][1] - done[j][1])))

print(d)

