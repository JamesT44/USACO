"""
ID: jameshu1
LANG: PYTHON3
TASK: runround
"""

import sys
from math import log10, floor

sys.stdin = open('runround.in', 'r')
sys.stdout = open('runround.out', 'w')

m = int(input())
i = m

while True:
    i += 1

    j = i
    pl = floor(log10(j) + 1)
    digits = []
    s = set()
    length = 0
    skip = False
    while j:
        x = j % 10
        if not (x % pl):
            i += 10 ** length - 1
            i -= i % (10 ** length)
            skip = True
            break
        if x in s:
            skip = True
            break
        s.add(x)
        digits.append(x)
        j //= 10
        length += 1
    if skip:
        continue
    digits = digits[::-1]
    if len(s) < length:
        continue
    visited = set()
    curr = 0
    while curr not in visited:
        visited.add(curr)
        curr += digits[curr]
        curr %= length
    if not curr and len(visited) == length:
        print(i)
        break
