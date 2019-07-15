"""
ID: jameshu1
LANG: PYTHON3
TASK: spin
"""

import sys

sys.stdin = open('spin.in', 'r')
sys.stdout = open('spin.out', 'w')

wheels = []
for _ in range(5):
    v, n, *w = map(int, input().split())
    degrees = set()
    for i in range(n):
        s, e = w[i * 2:i * 2 + 2]
        for d in range(s, s + e + 1):
            degrees.add(d % 360)
    wheels.append((v, degrees))

pos = [0, 0, 0, 0, 0]
t = 0
while True:
    d = set(range(360))
    for i, (v, degrees) in enumerate(wheels):
        d = {deg for deg in d if (deg - pos[i]) % 360 in degrees}
        pos[i] += v
        pos[i] %= 360
    if d:
        print(t)
        break
    t += 1
    if not any(pos):
        print("none")
        break
