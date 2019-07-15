"""
ID: jameshu1
LANG: PYTHON3
TASK: castle
"""

import sys

sys.stdin = open('castle.in', 'r')
sys.stdout = open('castle.out', 'w')

m, n = map(int, input().split())
grid = []
for _ in range(n):
    row = []
    for w in map(int, input().split()):
        row.append([w ^ 15, -1])
    grid.append(row)

sizes = []
component = 0
for x in range(n):
    for y in range(m):
        if grid[x][y][1] == -1:
            count = 0
            queue = {(x, y)}
            while queue:
                nx, ny = queue.pop()
                grid[nx][ny][1] = component
                count += 1

                if grid[nx][ny][0] & 2 and grid[nx - 1][ny][1] == -1:
                    queue.add((nx - 1, ny))
                if grid[nx][ny][0] & 4 and grid[nx][ny + 1][1] == -1:
                    queue.add((nx, ny + 1))
                if grid[nx][ny][0] & 8 and grid[nx + 1][ny][1] == -1:
                    queue.add((nx + 1, ny))
                if grid[nx][ny][0] & 1 and grid[nx][ny - 1][1] == -1:
                    queue.add((nx, ny - 1))

            sizes.append(count)
            component += 1

best = (0, -1, -1, "N")
for x in range(n):
    for y in range(m):
        if not grid[x][y][0] & 2 and x > 0 and grid[x][y][1] != grid[x - 1][y][1]:
            joined = sizes[grid[x][y][1]] + sizes[grid[x - 1][y][1]]
            if joined > best[0]:
                best = (joined, x, y, "N")
            elif joined == best[0]:
                if y < best[2]:
                    best = (joined, x, y, "N")
                elif y == best[2]:
                    if x >= best[1]:
                        best = (joined, x, y, "N")
        if not grid[x][y][0] & 4 and y < m - 1 and grid[x][y][1] != grid[x][y + 1][1]:
            joined = sizes[grid[x][y][1]] + sizes[grid[x][y + 1][1]]
            if joined > best[0]:
                best = (joined, x, y, "E")
            elif joined == best[0]:
                if y < best[2]:
                    best = (joined, x, y, "E")
                elif y == best[2]:
                    if x > best[1]:
                        best = (joined, x, y, "E")

print(len(sizes))
print(max(sizes))
print(best[0])
print(best[1] + 1, best[2] + 1, best[3])
