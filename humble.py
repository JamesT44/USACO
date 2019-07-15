"""
ID: jameshu1
LANG: PYTHON3
TASK: humble
"""

import sys
from math import inf

sys.stdin = open('humble.in', 'r')
sys.stdout = open('humble.out', 'w')

k, n = map(int, input().split())
s = list(map(int, sys.stdin.read().split()))

humble = [1]
ind = [0 for _ in s]
while len(humble) <= n:
    can = inf
    for i, p in enumerate(s):
        j = ind[i]
        while humble[j] * p <= humble[-1]:
            j += 1
        can = min(can, humble[j] * p)
        ind[i] = j
        if can == humble[-1] + 1:
            break
    humble.append(can)

print(humble[-1])
