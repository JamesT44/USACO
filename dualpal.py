"""
ID: jameshu1
LANG: PYTHON3
TASK: dualpal
"""

import sys

sys.stdin = open('dualpal.in', 'r')
sys.stdout = open('dualpal.out', 'w')

n, s = map(int, input().split())

i = s + 1
found = 0

while found < n:
    count = 0
    for base in range(2, 11):
        j = i
        res = []
        while j:
            res.append(j % base)
            j //= base
        if res == res[::-1]:
            count += 1
        if count == 2:
            print(i)
            found += 1
            break
    i += 1
