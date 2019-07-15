"""
ID: jameshu1
LANG: PYTHON3
TASK: stamps
"""

import sys
from math import inf

sys.stdin = open('stamps.in', 'r')
sys.stdout = open('stamps.out', 'w')

k, n = map(int, input().split())
stamps = list(map(int, sys.stdin.read().split()))
biggest = max(stamps)
mins = [inf for _ in range(biggest * (k + 1) + 4)]
mins[0] = 0

for stamp in stamps:
    for i in range(biggest * k + 4):
        if mins[i] < k:
            mins[i + stamp] = min(mins[i] + 1, mins[i + stamp])

res = 0
while mins[res + 1] <= k:
    res += 1

print(res)
