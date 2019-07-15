"""
ID: jameshu1
LANG: PYTHON3
TASK: beads
"""

import sys

sys.stdin = open('beads.in', 'r')
sys.stdout = open('beads.out', 'w')

n = int(input())
s = input()
best = 0

for i in range(29):
    left = s[:i][::-1] + s[::-1]
    right = s[i:] + s
    lcol, rcol = n, n

    j = 1
    while j < len(s):
        x = left[:j]
        if "b" in x and "r" in x:
            lcol = j - 1
            break
        j += 1

    j = 1
    while j < len(s):
        x = right[:j]
        if "b" in x and "r" in x:
            rcol = j - 1
            break
        j += 1

    best = max(best, rcol + lcol)

print(min(n, best))
