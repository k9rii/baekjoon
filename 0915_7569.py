import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split()) #가로, 세로, 높이
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, -1, 1, 0, 0] #n
dy = [-1, 1, 0, 0, 0, 0] #m
dz = [0, 0, 0, 0, -1, 1] #h
dq = deque()

def bfs():
    while dq:
        z, x, y = dq.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y]+1 #토마토 익는 일수 하루 추가
                    dq.append((nz, nx, ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1: #익은 토마토
                dq.append((i, j, k))
bfs()

is_not_complete = False
day = 0
#bfs끝난 후 다시 모든 칸 탐색
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0: #익지않은 토마토 여전히있다면
                is_not_complete = True
            day = max(day, graph[i][j][k])

if is_not_complete:
    print(-1)
else:
    print(day-1)
