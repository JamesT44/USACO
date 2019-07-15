"""
ID: jameshu1
LANG: PYTHON3
TASK: milk3
"""

import sys

sys.stdin = open('milk3.in', 'r')
sys.stdout = open('milk3.out', 'w')

limits = list(map(int, input().split()))

res = {limits[2]}
states = {(0, 0, limits[2])}
unvisited = [[0, 0, limits[2]]]

while unvisited:
    old = unvisited.pop(0)
    for start in range(3):
        if not old[start]:
            continue
        for destination in range(3):
            if start == destination or old[destination] == limits[destination]:
                continue
            poured = min(old[start], limits[destination] - old[destination])
            new = old[:]
            new[start] -= poured
            new[destination] += poured
            if tuple(new) not in states:
                unvisited.append(new)
                states.add(tuple(new))
                if not new[0]:
                    res.add(new[2])

print(" ".join(str(x) for x in sorted(res)))
