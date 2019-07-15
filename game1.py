"""
ID: jameshu1
LANG: PYTHON3
TASK: game1
"""

import sys
from itertools import accumulate

sys.stdin = open('game1.in', 'r')
sys.stdout = open('game1.out', 'w')

n = int(input())
board = [int(x) for x in sys.stdin.read().split()]
totals = [list(accumulate(board[i:])) for i in range(n)]
best = board[:]
for l in range(2, n + 1):
    best = [max(board[i] + totals[i + 1][l - 2] - best[i + 1],
                board[i + l - 1] + totals[i][l - 2] - best[i])
            for i in range(n - l + 1)]

print(best[0], totals[0][n - 1] - best[0])
