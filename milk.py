"""
ID: jameshu1
LANG: PYTHON3
TASK: milk
"""

import sys

sys.stdin = open('milk.in', 'r')
sys.stdout = open('milk.out', 'w')

n, m = map(int, input().split())
res = 0

for cost, capacity in sorted(tuple(map(int, input().split())) for _ in range(m)):
    if capacity >= n:
        res += cost * n
        break
    else:
        res += cost * capacity
        n -= capacity

print(res)
