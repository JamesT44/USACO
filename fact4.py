"""
ID: jameshu1
LANG: PYTHON3
TASK: fact4
"""

import sys

sys.stdin = open('fact4.in', 'r')
sys.stdout = open('fact4.out', 'w')

n = int(input())

fives = 0
i = 1
while 5 ** i <= n:
    fives += n // (5 ** i)
    i += 1

res = 1
for i in range(2, n + 1):
    j = i
    while not j % 5:
        j //= 5
    while not j % 2 and fives:
        fives -= 1
        j //= 2
    res *= j
    res %= 10

print(res)
