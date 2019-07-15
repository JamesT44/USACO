"""
ID: jameshu1
LANG: PYTHON3
TASK: maze1
"""

import sys

sys.stdin = open('maze1.in', 'r')
sys.stdout = open('maze1.out', 'w')

w, h = map(int, input().split())
c_grid = [list(input()) for _ in range(2 * h + 1)]

queue = []
grid = []
for y in range(h):
    row = []
    for x in range(w):
        cell = [c_grid[2 * y][2 * x + 1] == " ", c_grid[2 * y + 1][2 * x + 2] == " ",
                c_grid[2 * y + 2][2 * x + 1] == " ", c_grid[2 * y + 1][2 * x] == " ", False]
        if cell[0] and y == 0:
            cell[4] = True
            cell[0] = False
        if cell[1] and x == w - 1:
            cell[4] = True
            cell[1] = False
        if cell[2] and y == h - 1:
            cell[4] = True
            cell[2] = False
        if cell[3] and x == 0:
            cell[4] = True
            cell[3] = False
        if cell[4]:
            queue.append((1, x, y))
        row.append(cell)
    grid.append(row)

res = 1
while queue:
    level, x, y = queue.pop(0)
    res = max(res, level)
    if grid[y][x][0] and not grid[y - 1][x][4]:
        grid[y - 1][x][4] = True
        queue.append((level + 1, x, y - 1))
    if grid[y][x][1] and not grid[y][x + 1][4]:
        grid[y][x + 1][4] = True
        queue.append((level + 1, x + 1, y))
    if grid[y][x][2] and not grid[y + 1][x][4]:
        grid[y + 1][x][4] = True
        queue.append((level + 1, x, y + 1))
    if grid[y][x][3] and not grid[y][x - 1][4]:
        grid[y][x - 1][4] = True
        queue.append((level + 1, x - 1, y))

print(res)
