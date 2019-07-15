"""
ID: jameshu1
LANG: PYTHON3
TASK: friday
"""

import sys

sys.stdin = open('friday.in', 'r')
sys.stdout = open('friday.out', 'w')


def is_leap(yr):
    return (yr % 400 == 0) or (yr % 4 == 0 and yr % 100)


months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input())
counts = [0 for _ in range(7)]
day = 0
month = 0
year = 0

while year < n:
    counts[day] += 1
    day += months[month]
    if month == 1 and is_leap(1900 + year):
        day += 1
    day %= 7
    month += 1
    if month == 12:
        month = 0
        year += 1

print(*counts)
