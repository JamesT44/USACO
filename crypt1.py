"""
ID: jameshu1
LANG: PYTHON3
TASK: crypt1
"""

import sys
from itertools import product

sys.stdin = open('crypt1.in', 'r')
sys.stdout = open('crypt1.out', 'w')

n = int(input())
digits = set(input().split())
res = 0

for x in product(digits, repeat=3):
    xi = int("".join(x))
    candidates = [d for d in digits if set(str(xi * int(d))) <= digits and 100 <= xi * int(d) <= 999]
    if candidates:
        for y in product(candidates, repeat=2):
            p = xi * int("".join(y))
            if set(str(p)) <= digits and 1000 <= p <= 9999:
                res += 1

print(res)
