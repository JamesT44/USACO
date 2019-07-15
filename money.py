"""
ID: jameshu1
LANG: PYTHON3
TASK: money
"""

import sys

sys.stdin = open('money.in', 'r')
sys.stdout = open('money.out', 'w')

_, n = map(int, input().split())
coins = list(sorted(set(map(int, sys.stdin.read().split()))))
v = len(coins)

ways = [[0 for _ in range(v)] for _ in range(n + 1)]
ways[0] = [1 for _ in range(v)]
for i in range(1, n + 1):
    for j, coin in enumerate(coins):
        if i >= coins[j]:
            ways[i][j] += ways[i - coins[j]][j]
        if j >= 1:
            ways[i][j] += ways[i][j - 1]
print(ways[n][v - 1])
