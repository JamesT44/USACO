"""
ID: jameshu1
LANG: PYTHON3
TASK: skidesign
"""

import sys
from math import inf

sys.stdin = open('skidesign.in', 'r')
sys.stdout = open('skidesign.out', 'w')

n = int(input())
heights = list(sorted(int(input()) for _ in range(n)))

best = inf
for low in range(heights[0], heights[-1] - 16):
    res = 0
    for height in heights:
        if height < low:
            res += (low - height) ** 2
        elif height > low + 17:
            res += (height - low - 17) ** 2
    best = min(res, best)

print(best)
