#!/usr/bin/env python3


import sys

last = -1
count = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    i = int(l)
    if last != -1 and last < i:
        count += 1
    last = i
    print (i)

print(count)
