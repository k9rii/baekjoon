'''
<graph>
0: 갈 수 없는 땅
1: 갈 수 있는 땅
2. 목표 지점(시작점)
-
<visited>
0: 목표지점이거나 갈 수 없는 땅
1이상: 목표지점으로부터의 최단 거리
-1: 갈 수 있는 땅이지만 목표지점에서 도달할 수 없는 곳
'''
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = 0 #-1에서 0으로 초기화

    while dq: #덱이 빌 때까지 반복
        x, y = dq.popleft() #현재좌표
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i] #상하좌우이동

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1: #범위 안에 있고 아직 방문하지 않은 경우
                if graph[nx][ny]==0: #갈 수 없는 땅이면
                    visited[nx][ny] = 0 #0으로 설정하고 더 이상 탐색x
                elif graph[nx][ny]==1: #갈 수 있는 땅이면
                    visited[nx][ny] = visited[x][y]+1 #최단거리 업데이트
                    dq.append((nx, ny)) #큐에 추가해서 다음 탐색 대상으로 삼기

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1: #목표지점이고 미방문
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: #갈수없는땅이면
            print(0, end=' ') #0출력
        else:
            print(visited[i][j], end=' ')
    print()
