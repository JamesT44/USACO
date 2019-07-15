"""
ID: jameshu1
LANG: PYTHON3
TASK: fracdec
"""

import sys

sys.stdin = open('fracdec.in', 'r')
sys.stdout = open('fracdec.out', 'w')

n, d = map(int, input().split())
res = [str(n // d) + "."]

n %= d
n *= 10
prev = []
seen = set()
while n:
    if n in seen:
        res.insert(prev.index(n) + 1, "(")
        res.append(")")
        break
    prev.append(n)
    seen.add(n)
    res.append(str(n // d))
    n %= d
    n *= 10

res = "".join(res)

if res[-1] == ".":
    res += "0"

while res:
    print(res[:76])
    res = res[76:]
