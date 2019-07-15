"""
ID: jameshu1
LANG: PYTHON3
TASK: ride
"""

import sys
from functools import reduce

sys.stdin = open('ride.in', 'r')
sys.stdout = open('ride.out', 'w')

comet = reduce(lambda x, y: (x * y) % 47, [ord(c) - 64 for c in input()])
group = reduce(lambda x, y: (x * y) % 47, [ord(c) - 64 for c in input()])

if comet == group:
    print("GO")
else:
    print("STAY")
