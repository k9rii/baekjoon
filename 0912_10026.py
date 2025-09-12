import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dq = deque()

def bfs(x, y):
    dq.append((x, y))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited[x][y] = 1 #방문처리

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==graph[x][y] and visited[nx][ny]==0:
                #범위 안에 있고, 같은 색이고, 방문 안한 경우
                visited[nx][ny] = 1 #방문처리
                dq.append((nx, ny)) #큐에 넣기

#정상인
visited = [[0]*n for _ in range(n)]
result1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            result1 += 1

#적록색약
visited = [[0]*n for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i, j)
            result2 += 1

print(result1, result2)
