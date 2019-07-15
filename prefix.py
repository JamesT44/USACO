"""
ID: jameshu1
LANG: PYTHON3
TASK: prefix
"""

import sys

sys.stdin = open('prefix.in', 'r')
sys.stdout = open('prefix.out', 'w')

prefixes = [" "]
while prefixes[-1] != ".":
    prefixes.extend(list(input().split()))
prefixes = prefixes[1:-1]
pl = max(len(prefix) for prefix in prefixes)
s = sys.stdin.read().replace("\n", "")
sl = len(s)

trie = dict()
for prefix in prefixes:
    curr = trie
    for c in prefix:
        if c not in curr:
            curr[c] = dict()
        curr = curr[c]
    curr["#"] = True

best = 0
visited = {0}
queue = [0]

while queue:
    pos = queue.pop()
    if pos + pl < best and set(range(best - pl, best)) <= visited:
        break
    target = s[pos:]
    curr = trie
    for i, c in enumerate(target):
        if c in curr:
            curr = curr[c]
            if "#" in curr and pos + i + 1 not in visited:
                best = max(best, pos + i + 1)
                visited.add(pos + i + 1)
                queue.append(pos + i + 1)
        else:
            break

print(best)
