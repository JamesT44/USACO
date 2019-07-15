"""
ID: jameshu1
LANG: PYTHON3
TASK: agrinet
"""

import sys

sys.stdin = open('agrinet.in', 'r')
sys.stdout = open('agrinet.out', 'w')

n = int(input())
inp = sys.stdin.readlines()
data = list(map(int, " ".join(inp).split()))
matrix = [data[i:i + n] for i in range(0, n * n, n)]

remaining = set(range(1, n))
distance = matrix[0][:]

res = 0
while remaining:
    farm = min(remaining, key=distance.__getitem__)
    remaining.remove(farm)
    res += distance[farm]
    distance = [min(x, y) for x, y in zip(distance, matrix[farm])]

print(res)
