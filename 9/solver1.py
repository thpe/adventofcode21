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
inp = np.array(inp, dtype=np.int)

print('sorry, I lost the code. but it wasn\'t difficult :-)')
