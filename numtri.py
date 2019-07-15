"""
ID: jameshu1
LANG: PYTHON3
TASK: numtri
"""

import sys

sys.stdin = open('numtri.in', 'r')
sys.stdout = open('numtri.out', 'w')

r = int(input())
prev = [0]

for i in range(r):
    row = list(map(int, input().split()))
    row[0] += prev[0]
    for j in range(1, i):
        row[j] += max(prev[j - 1], prev[j])
    row[-1] += prev[-1]
    prev = row

print(max(prev))
