"""
ID: jameshu1
LANG: PYTHON3
TASK: barn1
"""

import sys

sys.stdin = open('barn1.in', 'r')
sys.stdout = open('barn1.out', 'w')

m, s, c = map(int, input().split())
stalls = [False for _ in range(s)]
occupied = list(sorted(int(input()) for _ in range(c)))

gaps = list(sorted(occupied[i + 1] - occupied[i] - 1 for i in range(c - 1)))

if m == 1:
    print(occupied[-1] - occupied[0] + 1)
else:
    print(occupied[-1] - occupied[0] + 1 - sum(gaps[-m + 1:]))
