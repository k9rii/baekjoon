'''
dfs
깊이가 5면 1 출력, 아니면 0 출력

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arrive = False #도착 확인용
A = [[] for _ in range(n+1)] #그래프 데이터 저장 인접 리스트
visited = [False]*(n+1) #방문기록 저장

def dfs(current, depth): #현재노드, 깊이
    global arrive
    if depth == 5: #dfs 깊이 5면 종료
        arrive = True
        return
    
    visited[current] = True #방문표시
    
    for i in A[current]:
        if not visited[i]:
            dfs(i, depth+1) #재귀호출마다 깊이 증가
    visited[current] = False #현재 노드의 모든 이웃 탐색하고 돌아왔을때, 다시 False로 미방문 처리

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a) #양방향 그래프

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

