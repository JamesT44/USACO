"""
ID: jameshu1
LANG: PYTHON3
TASK: sort3
"""

import sys

sys.stdin = open('sort3.in', 'r')
sys.stdout = open('sort3.out', 'w')

n = int(input())
r = [int(input()) for _ in range(n)]
c = [r.count(i) for i in range(1, 4)]
res = 0

c12 = r[:c[0]].count(2)
c13 = r[:c[0]].count(3)
c21 = r[c[0]:c[0] + c[1]].count(1)
c23 = r[c[0]:c[0] + c[1]].count(3)
c31 = r[-c[2]:].count(1)
c32 = r[-c[2]:].count(2)

s12 = min(c12, c21)
c12 -= s12
c21 -= s12
res += s12

s23 = min(c23, c32)
c23 -= s23
c32 -= s23
res += s23

s31 = min(c31, c13)
c31 -= s31
c13 -= s31
res += s31

res += (c12 + c13 + c21 + c23 + c31 + c32) // 3 * 2
print(res)
