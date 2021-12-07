#!/usr/bin/env python3


import sys
import re
import numpy as np
import pandas as pd


position = pd.read_csv(sys.argv[1], header=None)

position = np.array(position)

m = np.median(position)
d = np.sum(np.abs(position - m))


print(m)
print(d)

