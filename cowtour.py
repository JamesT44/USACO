"""
ID: jameshu1
LANG: PYTHON3
TASK: cowtour
"""

import sys
from math import inf

sys.stdin = open('cowtour.in', 'r')
sys.stdout = open('cowtour.out', 'w')

n = int(input())
location = [tuple(map(int, input().split())) for _ in range(n)]
adjacent = [list(map(int, list(input()))) for _ in range(n)]

distances = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    distances[i][i] = 0

    for j in range(n):
        if adjacent[i][j]:
            ix, iy = location[i]
            jx, jy = location[j]

            distances[i][j] = ((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5

for k in range(n):
    for i in range(n):
        for j in range(n):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

farthest = [max(distance for distance in distances[i] if distance != inf) for i in range(n)]
diameters = [0 for _ in range(n)]
remaining = set(range(n))
while remaining:
    first = remaining.pop()
    field = {i for i in range(n) if distances[first][i] != inf}
    diameter = max(farthest[i] for i in field)
    for i in field:
        # noinspection PyTypeChecker
        diameters[i] = diameter
    remaining -= field

res = inf
for i in range(n):
    for j in range(n):
        if distances[i][j] == inf:
            ix, iy = location[i]
            jx, jy = location[j]
            d = ((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5
            res = min(res, max(diameters[i], diameters[j], farthest[i] + farthest[j] + d))

print("{:0.6f}".format(res))
