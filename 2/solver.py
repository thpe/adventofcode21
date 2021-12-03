#!/usr/bin/env python3


import sys
import re

up = re.compile('up (\d)')
down = re.compile('down (\d)')
forward = re.compile('forward (\d)')

y = 0
x = 0

with open(sys.argv[1], 'r') as f:
  for l in f:
    m = up.match(l)
    if m:
      y -= int(m.group(1))
      print(f'up {m.group(1)}')
    m = down.match(l)
    if m:
      y += int(m.group(1))
      print(f'do {m.group(1)}')
    m = forward.match(l)
    if m:
      x += int(m.group(1))
      print(f'fo {m.group(1)}')

print(x)
print(y)
print(y*x)
