"""
ID: jameshu1
LANG: PYTHON3
TASK: heritage
"""

import sys

sys.stdin = open('heritage.in', 'r')
sys.stdout = open('heritage.out', 'w')

in_order = input()
pre_order = input()


def traverse(in_tree, pre_tree):
    root = pre_tree[0]
    i = in_tree.index(root)
    left, right = in_tree[:i], in_tree[i + 1:]
    if left:
        traverse(left, pre_tree[1:len(left) + 1])
    if right:
        traverse(right, pre_tree[-len(right):])
    print(root, end="")


traverse(in_order, pre_order)
print("")
