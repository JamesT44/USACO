"""
ID: jameshu1
LANG: PYTHON3
TASK: lamps
"""

import sys

sys.stdin = open('lamps.in', 'r')
sys.stdout = open('lamps.out', 'w')

n = int(input())
c = int(input())
ons = list(map(int, input().split()))[:-1]
offs = list(map(int, input().split()))[:-1]

res = []
if c == 0:
    res.append("1" * n)
elif c == 1:
    res.append("0" * n)
    res.append(("01" * (n // 2 + 1))[:n])
    res.append(("10" * (n // 2 + 1))[:n])
    res.append(("011" * (n // 3 + 1))[:n])
elif c >= 2:
    res.append("0" * n)
    res.append("1" * n)
    res.append(("01" * (n // 2 + 1))[:n])
    res.append(("10" * (n // 2 + 1))[:n])
    res.append(("100" * (n // 3 + 1))[:n])
    res.append(("001110" * (n // 6 + 1))[:n])
    res.append(("110001" * (n // 6 + 1))[:n])
if c > 2:
    res.append(("011" * (n // 3 + 1))[:n])

found = False
for r in sorted(res):
    for on in ons:
        if r[on - 1] != "1":
            break
    else:
        for off in offs:
            if r[off - 1] != "0":
                break
        else:
            print(r)
            found = True
if not found:
    print("IMPOSSIBLE")
