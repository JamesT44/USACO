"""
ID: jameshu1
LANG: PYTHON3
TASK: zerosum
"""

import sys
from itertools import product

sys.stdin = open('zerosum.in', 'r')
sys.stdout = open('zerosum.out', 'w')

n = int(input())
for signs in product(" +-", repeat=n - 1):
    res = ["1"]
    for i, sign in enumerate(signs):
        res.append(sign)
        res.append(str(i + 2))
    s = "".join(res)
    if eval(s.replace(" ", "")) == 0:
        print(s)
