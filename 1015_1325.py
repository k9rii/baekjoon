import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    dq = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    count = 1

    while dq:
        current = dq.popleft()
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)
                count += 1
    return count

result = 0
com = []
for i in range(1, n+1):
    hack = bfs(i)
    if hack > result:
        result = hack
        com = [i]
    elif hack == result:
        com.append(i)
print(*com)
