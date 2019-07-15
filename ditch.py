"""
ID: jameshu1
LANG: PYTHON3
TASK: ditch
"""

import sys
from collections import deque, defaultdict
from math import inf
import networkx as nx

sys.stdin = open('ditch.in', 'r')
# sys.stdout = open('ditch.out', 'w')

n, m = map(int, input().split())
"""
capacity = defaultdict(lambda : defaultdict(int))
for _ in range(n):
    s, e, c = map(int, input().split())
    capacity[s][e] = c

res = 0
while True:
    queue = deque([[[(0, 1)], set(), inf]])
    path = []
    r = 0
    while queue:
        path, p_set, r = queue.popleft()
        u = path[-1][1]
        if u == m:
            break
        for v in capacity[u]:
            if capacity[u][v] > 0 and (u, v) not in p_set:
                p_set.add((u, v))
                queue.append([path + [(u, v)], p_set, min(r, capacity[u][v])])
    else:
        break

    res += r
    for u, v in path[1:]:
        capacity[u][v] -= r
        capacity[v][u] += r

print(res)
"""

g = nx.Graph()
for _ in range(n):
    u, v, d = map(int, input().split())
    g.add_edge(u - 1, v - 1, capacity=d)
    print(g)
print(nx.algorithms.flow.maximum_flow(g, 0, 49))
