"""
ID: jameshu1
LANG: PYTHON3
TASK: ratios
"""

import sys
from math import gcd

sys.stdin = open('ratios.in', 'r')
sys.stdout = open('ratios.out', 'w')

goal = list(map(int, input().split()))
feeds = [list(map(int, input().split())) for _ in range(3)]
feeds = [list(row) for row in zip(*feeds)]


def det(mat):
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        res = 0
        for j, x in enumerate(mat[0]):
            d = det([row[:j] + row[j + 1:] for row in mat[1:]])
            if j % 2:
                res -= x * d
            else:
                res += x * d
        return res


num = []
den = det(feeds)
for i in range(3):
    matrix = [[goal[k] if i == j else x for j, x in enumerate(row)] for k, row in enumerate(feeds)]
    num.append(det(matrix))

g = gcd(gcd(gcd(num[0], num[1]), num[2]), den)
if den < 0:
    g = -g
num = [n // g for n in num]
den //= g

if not all(0 <= n < 100 for n in num):
    print("NONE")
else:
    print(*num, den)
