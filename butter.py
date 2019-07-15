"""
ID: jameshu1
LANG: PYTHON3
TASK: butter
"""

import sys
from math import inf
from collections import deque, Counter

sys.stdin = open('butter.in', 'r')
sys.stdout = open('butter.out', 'w')

n, p, c = map(int, input().split())
pastures = Counter(int(input()) - 1 for _ in range(n))

distance = [[inf for _ in range(p)] for _ in range(p)]
paths = [dict() for _ in range(p)]
for i in range(p):
    distance[i][i] = 0
for _ in range(c):
    i, j, d = map(int, input().split())
    paths[i - 1][j - 1] = d
    paths[j - 1][i - 1] = d

res = inf
for i in range(p):
    q = deque([i])
    visited = {i}
    while q:
        j = q.popleft()
        visited.remove(j)
        for k, dist in paths[j].items():
            if distance[i][j] + dist < distance[i][k]:
                distance[i][k] = distance[i][j] + dist
                if k not in visited:
                    visited.add(k)
                    q.append(k)

for i in range(p):
    x = 0
    for past, count in pastures.items():
        x += count * distance[i][past]
    res = min(x, res)

print(res)
