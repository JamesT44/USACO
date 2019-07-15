"""
ID: jameshu1
LANG: PYTHON3
TASK: fence9
"""

import sys
from math import ceil, floor

sys.stdin = open('fence9.in', 'r')
sys.stdout = open('fence9.out', 'w')

n, m, p = map(int, input().split())

print(sum(ceil(p - (i * (p - n) / m) - 1) - floor((i * n / m) + 1) + 1 for i in range(1, m)))
