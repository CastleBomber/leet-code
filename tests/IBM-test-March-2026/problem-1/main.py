#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 9th, 2026

    



*********************************************************
"""

from typing import Optional, List, Dict, Tuple, Set
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify
import math
import bisect
import itertools
import functools
import os
import random
import re
import sys



#
# Complete the 'addNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT a
#  2. FLOAT b
#

def addNumbers(a, b):
    c = a + b
    return math.floor(c)
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = float(input().strip())
    #b = float(input().strip())

    a = 1.1
    b = 3.89

    result = addNumbers(a, b)
    print(result)
    
    # fptr.write(str(result) + '\n')
    # fptr.close()