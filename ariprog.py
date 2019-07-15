"""
ID: jameshu1
LANG: PYTHON3
TASK: ariprog
"""

import sys
from bisect import insort

sys.stdin = open('ariprog.in', 'r')
sys.stdout = open('ariprog.out', 'w')

n = int(input())
m = int(input())

limit = 2 * m * m
bis = set()
s_bis = []
for p in range(m + 1):
    for q in range(p, m + 1):
        x = p ** 2 + q ** 2
        bis.add(x)
        insort(s_bis, x)

delta = [0 for _ in range(125001)]
last = 0
for bi in s_bis:
    delta[last] = bi - last
    last = bi
delta[0] = 1
delta[last] = 1

res = []
for a in bis:
    maxi = ((limit - a) // (n - 1)) + 1
    d = delta[a]
    while d <= maxi:
        curr = a
        for i in range(1, n):
            curr += d
            if not delta[curr]:
                break
        else:
            insort(res, (d, a))
        d += 1

if res:
    for d, a in res:
        print(a, d)
else:
    print("NONE")
