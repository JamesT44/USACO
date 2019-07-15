"""
ID: jameshu1
LANG: PYTHON3
TASK: camelot
"""

import sys
from math import inf

sys.stdin = open('camelot.in', 'r')
sys.stdout = open('camelot.out', 'w')

r, c = map(int, input().split())
kx, ky = input().split()
kx, ky = ord(kx) - ord("A"), int(ky) - 1

moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
k_dist = [[0 for _ in range(r)] for _ in range(c)]
k_cost = [[0 for _ in range(r)] for _ in range(c)]

for x in range(c):
    for y in range(r):
        k_dist[x][y] = k_cost[x][y] = max(abs(kx - x), abs(ky - y))

cost = [[0 for _ in range(r)] for _ in range(c)]
for line in sys.stdin:
    parts = line.split()
    for i in range(0, len(parts), 2):
        nx, ny = parts[i:i + 2]
        nx, ny = ord(nx) - ord("A"), int(ny) - 1
        n_dist = [[inf for _ in range(r)] for _ in range(c)]
        nk_dist = [[inf for _ in range(r)] for _ in range(c)]
        n_dist[nx][ny] = 0
        maximum = nk_dist[nx][ny] = k_dist[nx][ny]

        d = 0
        while d <= maximum:
            for x in range(c):
                for y in range(r):
                    if n_dist[x][y] == d:
                        f = 0
                        for dx, dy in moves:
                            new_x, new_y = x + dx, y + dy
                            if c > new_x >= 0 <= new_y < r and n_dist[new_x][new_y] > d + 1:
                                f = 1
                                n_dist[new_x][new_y] = d + 1
                        zz = d + k_dist[x][y]
                        if nk_dist[x][y] > zz:
                            nk_dist[x][y] = zz
                            f = max(f, k_dist[x][y])
                        maximum = max(maximum, d + f)
                    if nk_dist[x][y] == d:
                        f = 0
                        for dx, dy in moves:
                            new_x, new_y = x + dx, y + dy
                            if c > new_x >= 0 <= new_y < r and nk_dist[new_x][new_y] > d + 1:
                                f = 1
                                nk_dist[new_x][new_y] = d + 1
                        maximum = max(maximum, d + f)
            d += 1

        for x in range(c):
            for y in range(r):
                cost[x][y] += n_dist[x][y]
                # noinspection PyTypeChecker
                k_cost[x][y] = min(k_cost[x][y], nk_dist[x][y] - n_dist[x][y])

res = inf
for x in range(c):
    for y in range(r):
        res = min(res, cost[x][y] + k_cost[x][y])

print(res)
