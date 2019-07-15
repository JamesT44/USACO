"""
ID: jameshu1
LANG: PYTHON3
TASK: namenum
"""

import sys

sys.stdin = open('namenum.in', 'r')
sys.stdout = open('namenum.out', 'w')
names = open("dict.txt", "r")

letters = {2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PRS", 8: "TUV", 9: "WXY"}
n = input()
found = False

for name in names:
    name = name.strip()
    if len(name) == len(n):
        for i, d in enumerate(n):
            if name[i] not in letters[int(d)]:
                break
        else:
            print(name)
            found = True

if not found:
    print("NONE")
