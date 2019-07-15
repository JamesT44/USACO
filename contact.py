"""
ID: jameshu1
LANG: PYTHON3
TASK: contact
"""

import sys
from collections import Counter
sys.stdin = open('contact.in', 'r')
sys.stdout = open('contact.out', 'w')

a, b, n = map(int, input().split())
s = "".join(line.strip() for line in sys.stdin.readlines())
sl = len(s) + 1

counts = Counter()
for length in range(a, b + 1):
    counts.update([s[i:i + length] for i in range(sl - length)])

common = counts.most_common()
count = 0
while common and count < n:
    p, f = common.pop(0)
    print(f)

    ps = [p]
    while common and common[0][1] == f:
        p = common.pop(0)[0]
        ps.append(p)

    ps = sorted(ps, key=lambda x: (len(x), x))
    while ps:
        print(*ps[:6])
        ps = ps[6:]
    count += 1
