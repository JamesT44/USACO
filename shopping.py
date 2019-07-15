"""
ID: jameshu1
LANG: PYTHON3
TASK: shopping
"""

import sys
from math import inf
from collections import deque

sys.stdin = open('shopping.in', 'r')
# sys.stdout = open('shopping.out', 'w')

ci = 0
cmap = dict()

s = int(input())
offers = dict()
for j_ in range(s):
    n, *p, price = map(int, input().split())
    quantities = [0, 0, 0, 0, 0]
    for i in range(0, 2 * n, 2):
        if p[i] not in cmap:
            cmap[p[i]] = ci
            ci += 1
        quantities[cmap[p[i]]] = p[i + 1]
    x = tuple(quantities)
    if x in offers:
        offers[x] = min(offers[x], price)
    else:
        offers[x] = price

if s:
    b = int(input())
    basket = [0, 0, 0, 0, 0]
    for _ in range(b):
        c, k, p = map(int, input().split())
        if c not in cmap:
            cmap[c] = ci
            ci += 1
        basket[cmap[c]] = k
        x = tuple(1 if i == cmap[c] else 0 for i in range(5))
        if x in offers:
            offers[x] = min(offers[x], p)
        else:
            offers[x] = p

    res = inf
    queue = deque([basket[:]])
    visited = {tuple(basket): 0}
    while queue:
        basket = queue.popleft()
        cost = visited[tuple(basket)]
        if not any(basket):
            res = min(res, cost)
            continue
        for quantities, price in offers.items():
            n_basket = basket[:]
            for i in range(5):
                n_basket[i] -= quantities[i]
                if n_basket[i] < 0:
                    break
            else:
                if tuple(n_basket) not in visited:
                    queue.append(n_basket)
                    visited[tuple(n_basket)] = cost + price
                else:
                    for i, m_basket in enumerate(queue):
                        if m_basket == n_basket:
                            visited[tuple(n_basket)] = min(visited[tuple(n_basket)], cost + price)
                            break

    print(res)
else:
    res = 0
    b = int(input())
    for _ in range(b):
        _, k, p = map(int, input().split())
        res += k * p

    print(res)
