"""
ID: jameshu1
LANG: PYTHON3
TASK: kimbits
"""

import sys

sys.stdin = open('kimbits.in', 'r')
sys.stdout = open('kimbits.out', 'w')

n, l, i = map(int, input().split())
i -= 1

memo = dict()


def size(x, y):
    if not x or not y:
        return 1
    elif (x, y) in memo:
        return memo[(x, y)]
    else:
        memo[(x, y)] = size(x - 1, y) + size(x - 1, y - 1)
        return memo[(x, y)]


res = []
while n:
    s = size(n - 1, l)
    if s <= i:
        res.append("1")
        l -= 1
        i -= s
    else:
        res.append("0")
    n -= 1

print("".join(res))
