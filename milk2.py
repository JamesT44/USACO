"""
ID: jameshu1
LANG: PYTHON3
TASK: milk2
"""

from bisect import insort
import sys

sys.stdin = open('milk2.in', 'r')
sys.stdout = open('milk2.out', 'w')

n = int(input())
intervals = []

for i in range(n):
    start, end = map(int, input().split())
    insort(intervals, [start, end])

merged = [intervals.pop(0)]

for interval in intervals:
    if interval[0] > merged[-1][1]:
        merged.append(interval)
    elif interval[1] > merged[-1][1]:
        merged[-1][1] = interval[1]

longest = 0
for start, end in merged:
    longest = max(longest, end - start)

idlest = 0
for i in range(1, len(merged)):
    idlest = max(idlest, merged[i][0] - merged[i - 1][1])

print(longest, idlest)
