"""
ID: jameshu1
LANG: PYTHON3
TASK: rockers
"""

import sys
from collections import defaultdict

sys.stdin = open('rockers.in', 'r')
sys.stdout = open('rockers.out', 'w')

n, t, m = map(int, input().split())
lengths = [0] + list(map(int, input().split()))

dp = defaultdict(int)
res = 0
for i in range(m):
    for j in range(t + 1):
        for k in range(n + 1):
            for l in range(k + 1, n + 1):
                if j + lengths[l] <= t:
                    dp[(i, j + lengths[l], l)] = max(dp[(i, j + lengths[l], l)], dp[(i, j, k)] + 1)
                else:
                    dp[(i + 1, lengths[l], l)] = max(dp[(i + 1, lengths[l], l)], dp[(i, j, k)] + 1)
            res = max(res, dp[(i, j, k)])

print(res)
