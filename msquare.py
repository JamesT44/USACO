"""
ID: jameshu1
LANG: PYTHON3
TASK: msquare
"""

import sys

sys.stdin = open('msquare.in', 'r')
sys.stdout = open('msquare.out', 'w')

target = tuple(map(int, input().split()))
visited = {tuple(range(1, 9))}
queue = [(list(range(1, 9)), "")]

while target not in visited:
    seq, path = queue.pop(0)

    a = seq[::-1]
    ta = tuple(a)
    if ta not in visited:
        visited.add(ta)
        queue.append((a, path + "A"))

    b = [seq[3]] + seq[:3] + seq[5:] + [seq[4]]
    tb = tuple(b)
    if tb not in visited:
        visited.add(tb)
        queue.append((b, path + "B"))

    c = seq[:]
    c[1], c[2], c[5], c[6] = c[6], c[1], c[2], c[5]
    tc = tuple(c)
    if tc not in visited:
        visited.add(tc)
        queue.append((c, path + "C"))

for seq, path in queue:
    if seq == list(target):
        print(len(path))
        print(path)
        break
