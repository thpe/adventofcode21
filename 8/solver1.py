#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd


digits = pd.read_csv(sys.argv[1], sep=' ', header=None)
l = digits.applymap(lambda x: len(x))

l = l[[11, 12, 13, 14]]
ones = (l == 2).sum().sum()
fours = (l == 4).sum().sum()
sevens = (l == 3).sum().sum()
eights = (l == 7).sum().sum()
print(f'solution: {ones+fours+sevens+eights}')
