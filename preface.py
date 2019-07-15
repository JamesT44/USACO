"""
ID: jameshu1
LANG: PYTHON3
TASK: preface
"""

import sys
from collections import Counter

sys.stdin = open('preface.in', 'r')
sys.stdout = open('preface.out', 'w')

n = int(input())

values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
          (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
counts = Counter()
for i in range(1, n + 1):
    roman = ""
    rem = i
    for val, numerals in values:
        if rem >= val:
            roman += numerals * (rem // val)
        rem %= val
    counts.update(roman)

for c in "IVXLCDM":
    if c in counts:
        print(c, counts[c])
    else:
        break
