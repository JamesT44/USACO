"""
ID: jameshu1
LANG: PYTHON3
TASK: combo
"""

import sys

sys.stdin = open('combo.in', 'r')
sys.stdout = open('combo.out', 'w')

n = int(input())
j = list(map(int, input().split()))
m = list(map(int, input().split()))
res = set()

for da in range(-2, 3):
    for db in range(-2, 3):
        for dc in range(-2, 3):
            res.add(((j[0] + da) % n, (j[1] + db) % n, (j[2] + dc) % n))
            res.add(((m[0] + da) % n, (m[1] + db) % n, (m[2] + dc) % n))

print(len(res))
