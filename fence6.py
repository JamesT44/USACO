"""
ID: jameshu1
LANG: PYTHON3
TASK: fence6
"""

import sys
from math import inf

sys.stdin = open('fence6.in', 'r')
sys.stdout = open('fence6.out', 'w')

n = int(input())
fence = [[0, set(), set()] for _ in range(n + 1)]
for _ in range(n):
    s, ls, _, _ = map(int, input().split())
    left, right = set(map(int, input().split())), set(map(int, input().split()))
    fence[s] = [ls, left, right]

res = inf
for i in range(1, n + 1):
    remaining = set(range(1, n + 1))
    dist = [inf for _ in range(n + 1)]
    prev = [0 for _ in range(n + 1)]
    for node in fence[i][1]:
        dist[node] = fence[node][0]
        prev[node] = i

    while i in remaining:
        j = min(remaining, key=dist.__getitem__)
        remaining.remove(j)
        if prev[j] in fence[j][1]:
            neighbours = fence[j][2]
        else:
            neighbours = fence[j][1]
        for neighbour in neighbours:
            if dist[neighbour] > dist[j] + fence[neighbour][0]:
                dist[neighbour] = dist[j] + fence[neighbour][0]
                prev[neighbour] = j
    res = min(res, dist[i])

print(res)
