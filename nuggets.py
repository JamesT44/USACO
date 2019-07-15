"""
ID: jameshu1
LANG: PYTHON3
TASK: nuggets
"""

import sys
from math import gcd
from functools import reduce

sys.stdin = open('nuggets.in', 'r')
sys.stdout = open('nuggets.out', 'w')

n = int(input())
nuggets = [int(input()) for _ in range(n)]

if reduce(gcd, nuggets) > 1:
    print(0)
else:
    possible = [False for _ in range(256)]
    possible[0] = True

    last = 0
    for i in range(2000000000):
        if i > 256 + last:
            break
        if not possible[i % 256]:
            last = i
        else:
            possible[i % 256] = False
            for nugget in nuggets:
                possible[(i + nugget) % 256] = True

    print(last)
