"""
ID: jameshu1
LANG: PYTHON3
TASK: wormhole
"""

import sys


sys.stdin = open('wormhole.in', 'r')
sys.stdout = open('wormhole.out', 'w')


class Cord(object):
    def __init__(self, cx, cy):
        self.x = cx
        self.y = cy
        self.paired = None

    def next(self):
        for d in cords:
            if d.y == self.y and d.x > self.x:
                return d
        return None


n = int(input())
cords = []
for i in range(n):
    x, y = map(int, input().split())
    cords.append(Cord(x, y))
cords.sort(key=lambda z: z.x)


def pair(co):
    c1, c2 = co[0], co[1]
    c1.paired = c2
    c2.paired = c1


def pairs(s):
    li = list(s)

    if len(li) == 2:
        return [[(li[0], li[1])]]

    result = []
    for j in range(1, len(s)):
        rests = pairs(s - {li[0], li[j]})
        result += [[(li[0], li[j])] + rest for rest in rests]
    return result


pl = pairs(set(cords))

count = 0
for pairings in pl:
    for p in pairings:
        pair(p)

    loop = False
    for c in set(cords):
        route = set()

        while True:
            ni = c.paired
            if ni in route:
                loop = True
                break
            route |= {ni}
            if ni.next() is None:
                break
            else:
                c = ni.next()

        if loop:
            break
    if loop:
        count += 1

print(count)
