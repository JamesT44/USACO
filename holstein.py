"""
ID: jameshu1
LANG: PYTHON3
TASK: holstein
"""

import sys
from itertools import combinations

sys.stdin = open('holstein.in', 'r')
sys.stdout = open('holstein.out', 'w')

v = int(input())
req = list(map(int, input().split()))
g = int(input())
feeds = [list(map(int, input().split())) + [i + 1] for i in range(g)]

found = False
for res in range(1, g + 1):
    for scoops in combinations(feeds, res):
        total = [sum(i) for i in zip(*scoops)]
        if all(total[i] >= req[i] for i in range(v)):
            print(res, " ".join(str(scoop[-1]) for scoop in scoops))
            found = True
            break

    if found:
        break
