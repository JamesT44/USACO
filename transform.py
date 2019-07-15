"""
ID: jameshu1
LANG: PYTHON3
TASK: transform
"""

import sys

sys.stdin = open('transform.in', 'r')
sys.stdout = open('transform.out', 'w')

n = int(input())
before = [list(input()) for _ in range(n)]
after = [list(input()) for _ in range(n)]

if [list(row) for row in zip(*before[::-1])] == after:
    print(1)
elif [row[::-1] for row in before[::-1]] == after:
    print(2)
elif [list(row) for row in zip(*before)][::-1] == after:
    print(3)
elif [row[::-1] for row in before] == after:
    print(4)
elif [list(row) for row in zip(*before[::-1])][::-1] == after:
    print(5)
elif before[::-1] == after:
    print(5)
elif [list(row) for row in zip(*before)] == after:
    print(5)
elif before == after:
    print(6)
else:
    print(7)
