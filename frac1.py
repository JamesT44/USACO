"""
ID: jameshu1
LANG: PYTHON3
TASK: frac1
"""

import sys
from bisect import insort
from fractions import Fraction
from math import gcd

sys.stdin = open('frac1.in', 'r')
sys.stdout = open('frac1.out', 'w')

n = int(input())

res = []

for d in range(2, n + 1):
    for num in range(1, d):
        if gcd(num, d) == 1:
            insort(res, Fraction(num, d))

print("0/1")
for f in res:
    print(f)
print("1/1")
