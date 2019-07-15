"""
ID: jameshu1
LANG: PYTHON3
TASK: inflate
"""

import sys

sys.stdin = open('inflate.in', 'r')
sys.stdout = open('inflate.out', 'w')

m, n = map(int, input().split())

best = [0 for _ in range(m + 1)]
for _ in range(n):
    p, minutes = map(int, input().split())
    for i in range(minutes, m + 1):
        best[i] = max(best[i], best[i - minutes] + p)

print(best[-1])
