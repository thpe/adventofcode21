#!/usr/bin/env python3


import copy
import sys
import re
import numpy as np
import pandas as pd
from scipy.ndimage.measurements import label

cave = pd.read_csv(sys.argv[1], sep='-', header=None)
cave = np.array(cave)
print(cave)

nodes = []
nodeidx = {}
name = []
adj = []
once = []
start = None
end = None

def add (f, t):
  print(f'add {f} {t}')
  if t == 'start':
    return
  if f not in nodeidx:
    if f != "end":
      adj.append([t])
    else:
      adj.append([])
    once.append(f[0].islower())
    nodeidx[f] = len(once) - 1
    name.append(f)
  else:
    idx = nodeidx[f]
    if f != "end":
      adj[idx].append(t)

for edge in range(cave.shape[0]):
  f = cave[edge, 0]
  t = cave[edge, 1]
  add(f, t)
  add(t, f)

print(nodeidx)
print(adj)
print(once)


visited = [False for i in range(len(once))]
queue = []
queue.append(nodeidx['start'])

count = 0


def dfs(node, visited, count, path, double):
#    print(f'dfs {node} {name[node]} {visited} {count} {path}')
    origpath = copy.copy(path)
    if not visited[node]:
        path = copy.copy(origpath)
        path.append(name[node])
        if once[node]:
          visited[node] = True
        for k in adj[node]:
            if k == 'end':
              path.append(k)
              print(path)
              count+=1
            else:
              (v, count) = dfs(nodeidx[k], copy.copy(visited), count, copy.copy(path), double)
    elif not double:
        path = copy.copy(origpath)
        path.append(name[node])
        if once[node]:
          visited[node] = True
        for k in adj[node]:
            if k == 'end':
              path.append(k)
              print(path)
              count+=1
            else:
              (v, count) = dfs(nodeidx[k], copy.copy(visited), count, copy.copy(path), True)
    return (visited, count)


(visited, count) = dfs (nodeidx['start'], visited, count, [], False)
print(count)
