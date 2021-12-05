#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd

inp = []

numbers = pd.read_csv(sys.argv[2], header=None)
board = pd.read_fwf(sys.argv[1], header=None)

numbers = np.array(numbers)
board = np.array(board)

board = board.reshape((100,5,5))
mask = np.zeros(board.shape)

quit = False
print(board.shape)
for n in numbers.flatten():
  if quit:
    break
  n = int(n)
  print(n)
  for b in range(board.shape[0]):
    if quit:
      break
    for x in range(board.shape[1]):
      if quit:
        break
      for y in range(board.shape[2]):
        if board[b][x][y] == n:
          mask[b][x][y] = 1
          print(mask[b])
          if np.all(mask[b,:,y] == 1):
            print(f'board {b} won')
            print(mask[b])
            print(board[b])
            a = np.ma.array(board[b], mask = mask[b])
            s = np.sum(a) * n
            print(a)
            print(s)
            quit = True
            break
          if np.all(mask[b,x,:] == 1):
            print(f'board {b} won')
            print(mask[b])
            print(board[b])
            quit = True
            break


