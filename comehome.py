"""
ID: jameshu1
LANG: PYTHON3
TASK: comehome
"""

import sys
from bisect import insort
from math import inf

sys.stdin = open('comehome.in', 'r')
sys.stdout = open('comehome.out', 'w')

p = int(input())

dists = [[inf for _ in range(52)] for _ in range(52)]
for i in range(52):
    dists[i][i] = 0
for _ in range(p):
    i, j, d = input().split()
    i, j, d = ord(i) - 39, ord(j) - 39, int(d)
    if i >= 58:
        i -= 58
    if j >= 58:
        j -= 58
    dists[i][j] = min(dists[i][j], d)
    dists[j][i] = dists[i][j]

queue = []
for i in range(51):
    d = dists[51][i]
    if d < inf:
        insort(queue, [d, i])

visited = {51}
while True:
    d, i = queue.pop(0)
    if i >= 26:
        print(chr(i + 39), d)
        break
    if i in visited:
        continue
    visited.add(i)
    for j in range(51):
        if i == j:
            continue
        if dists[i][j] < inf:
            insort(queue, [d + dists[i][j], j])
