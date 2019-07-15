"""
ID: jameshu1
LANG: PYTHON3
TASK: subset
"""

import sys
from collections import defaultdict

sys.stdin = open('subset.in', 'r')
sys.stdout = open('subset.out', 'w')

n = int(input())
target = n * (n + 1) // 2

if target % 2:
    print(0)
else:
    target = (target // 2)
    ways = defaultdict(int)
    ways[0] = 1
    for i in range(1, n + 1):
        sways = ways.copy()
        for v, c in ways.items():
            sways[v + i] += c
        ways = sways
    print(ways[target] // 2)
