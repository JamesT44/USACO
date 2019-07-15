"""
ID: jameshu1
LANG: PYTHON3
TASK: fence
"""

import sys
from collections import Counter

sys.stdin = open('fence.in', 'r')
sys.stdout = open('fence.out', 'w')

f = int(input())
fences = Counter()
c = Counter()

m = 0
for _ in range(f):
    i, j = map(int, input().split())
    if i > j:
        i, j = j, i
    fences[(i, j)] += 1
    m = max(m, i, j)
    c.update((i, j))

ends = []
for i in range(1, m + 1):
    if c[i] % 2:
        ends.extend([i, c[i]])
if ends:
    i = ends[0]
else:
    i = 1

tour = [i]
while fences:
    for j in range(1, m + 1):
        if ends and j == ends[2] and ends[3] == 1 and len(fences) > 1:
            continue
        if (i, j) in fences:
            fences[(i, j)] -= 1
            fences = +fences
            i = j
            tour.append(j)
            if ends and j == ends[2]:
                ends[3] -= 1
            break
        elif (j, i) in fences:
            fences[(j, i)] -= 1
            fences = +fences
            i = j
            tour.append(j)
            if ends and j == ends[2]:
                ends[3] -= 1
            break
    else:
        while fences:
            remaining = set()
            for i, j in fences:
                remaining.update((i, j))
            for ind, i in enumerate(tour[::-1]):
                if i not in remaining:
                    continue
                remaining = sorted(remaining)
                s_tour = []
                while fences:
                    for j in remaining:
                        if (i, j) in fences:
                            fences[(i, j)] -= 1
                            fences = +fences
                            i = j
                            s_tour.append(j)
                            break
                        elif (j, i) in fences:
                            fences[(j, i)] -= 1
                            fences = +fences
                            i = j
                            s_tour.append(j)
                            break
                    else:
                        break
                tour = tour[:-ind] + s_tour[:] + tour[-ind:]
                break

for i in tour:
    print(i)
