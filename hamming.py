"""
ID: jameshu1
LANG: PYTHON3
TASK: hamming
"""

import sys

sys.stdin = open('hamming.in', 'r')
sys.stdout = open('hamming.out', 'w')

n, b, d = map(int, input().split())
res = [0]

i = (1 << d) - 1
while len(res) < n:
    for r in res:
        if bin(r ^ i).count("1") < d:
            break
    else:
        res.append(i)
    i += 1

while res:
    print(*res[:10])
    res = res[10:]
