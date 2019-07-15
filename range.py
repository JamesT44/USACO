"""
ID: jameshu1
LANG: PYTHON3
TASK: range
"""

import sys

sys.stdin = open('range.in', 'r')
sys.stdout = open('range.out', 'w')

n = int(input())

biggest = [0 for _ in range(n + 1)]
res = [0 for _ in range(n + 1)]
for _ in range(n):
    prev = 0
    biggest[0] = 0
    for i, c in enumerate(input()):
        if c != "1":
            prev, biggest[i + 1] = biggest[i + 1], 0
            continue
        prev, biggest[i + 1] = biggest[i + 1], min(biggest[i], prev, biggest[i + 1]) + 1

        if biggest[i + 1] >= 2:
            res[biggest[i + 1]] += 1

size = 2
while True:
    x = sum(res[size:])
    if not x:
        break
    print(size, x)
    size += 1
