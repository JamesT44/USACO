"""
ID: jameshu1
LANG: PYTHON3
TASK: palsquare
"""

import sys

sys.stdin = open('palsquare.in', 'r')
sys.stdout = open('palsquare.out', 'w')

n = int(input())
digits = "0123456789ABCDEFGHIJ"

for i in range(1, 301):
    i2 = i ** 2
    res = []
    while i2:
        res.append(digits[i2 % n])
        i2 //= n
    if res == res[::-1]:
        j = i
        ni = []
        while j:
            ni.append(digits[j % n])
            j //= n
        print("".join(ni[::-1]), "".join(res))
