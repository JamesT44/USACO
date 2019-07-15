"""
ID: jameshu1
LANG: PYTHON3
TASK: concom
"""

import sys
from bisect import insort

sys.stdin = open('concom.in', 'r')
sys.stdout = open('concom.out', 'w')

n = int(input())

m = 0
controlling = dict()
for _ in range(n):
    i, j, p = map(int, input().split())
    m = max(m, i, j)

    if i in controlling:
        controlling[i][j] = p
    else:
        controlling[i] = {j: p}

for c in range(1, m + 1):
    if c not in controlling:
        continue

    percents = {i: 0 for i in range(1, m + 1)}
    percents[c] = 100
    current = []
    remaining = set(range(1, m + 1))
    while True:
        for d in remaining:
            if percents[d] > 50:
                insort(current, d)
                remaining.discard(d)
                if d in controlling:
                    for k, p in controlling[d].items():
                        if k in remaining:
                            percents[k] += p
                break
        else:
            break

    for d in current:
        if d != c:
            print(c, d)
