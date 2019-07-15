"""
ID: jameshu1
LANG: PYTHON3
TASK: nocows
"""

import sys

sys.stdin = open('nocows.in', 'r')
sys.stdout = open('nocows.out', 'w')

n, k = map(int, input().split())
dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
for j in range(1, k + 1):
    dp[1][j] = 1

for i in range(2, n + 1):
    for j in range(1, k + 1):
        for x in range(1, i - 1):
            dp[i][j] += dp[x][j - 1] * dp[i - x - 1][j - 1]
        dp[i][j] %= 9901

print((dp[n][k] - dp[n][k - 1]) % 9901)
