"""
ID: jameshu1
LANG: PYTHON3
TASK: test
"""

import sys

sys.stdin = open('test.in', 'r')
sys.stdout = open('test.out', 'w')

x, y = map(int, input().split())
total = x + y

print(total)
