import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split()) #가로세로
graph = [list(map(int, input().split())) for _ in range(n)]
'''
<graph>
1: 익은 토마토
0: 익지 않은 토마토
-1: 토마토없음
'''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dq = deque()
result = 0
count_zero = 0 #익지않은 토마토 개수

#큐에 모든 익은 토마토 위치 넣고, 익지않은토마토 개수 세기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dq.append((i, j, 0)) #(x, y, 일수)
        elif graph[i][j] == 0:
            count_zero += 1

while dq:
    x, y, days = dq.popleft()
    result = max(result, days)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            graph[nx][ny] = 1
            dq.append((nx, ny, days+1))
            count_zero -= 1

if count_zero == 0:
    print(result)
else:
    print(-1)
