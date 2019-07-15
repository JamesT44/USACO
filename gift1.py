"""
ID: jameshu1
LANG: PYTHON3
TASK: gift1
"""

from collections import OrderedDict
import sys

sys.stdin = open('gift1.in', 'r')
sys.stdout = open('gift1.out', 'w')

np = int(input())
accounts = OrderedDict()
for i in range(np):
    accounts[input()] = 0

for i in range(np):
    giver = input()
    amount, ng = map(int, input().split())
    if ng:
        gift = amount // ng
        accounts[giver] -= gift * ng
        for j in range(ng):
            accounts[input()] += gift

for name, balance in accounts.items():
    print(name, balance)
