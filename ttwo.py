"""
ID: jameshu1
LANG: PYTHON3
TASK: ttwo
"""

import sys

sys.stdin = open('ttwo.in', 'r')
sys.stdout = open('ttwo.out', 'w')

fx, fy = -1, -1
fdx, fdy = 0, -1

cx, cy = -1, -1
cdx, cdy = 0, -1

obstacles = set()
for i in range(10):
    obstacles.add((-1, i))
    obstacles.add((10, i))
    obstacles.add((i, -1))
    obstacles.add((i, 10))

for y in range(10):
    for x, c in enumerate(input()):
        if c == "*":
            obstacles.add((x, y))
        elif c == "F":
            fx, fy = x, y
        elif c == "C":
            cx, cy = x, y

states = set()
minutes = 1
while True:
    if (fx, fy, fdx, fdy, cx, cy, cdx, cdy) in states:
        print(0)
        break
    states.add((fx, fy, fdx, fdy, cx, cy, cdx, cdy))

    if (fx + fdx, fy + fdy) in obstacles:
        fdx, fdy = -fdy, fdx
    else:
        fx += fdx
        fy += fdy

    if (cx + cdx, cy + cdy) in obstacles:
        cdx, cdy = -cdy, cdx
    else:
        cx += cdx
        cy += cdy

    if fx == cx and fy == cy:
        print(minutes)
        break

    minutes += 1
