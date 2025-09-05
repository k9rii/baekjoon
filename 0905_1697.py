import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v==k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and array[next_v] == 0: #유효 범위 내에 있고 아직 방문하지 않았다면(0)
                array[next_v] = array[v] + 1
                q.append(next_v)

MAX = 100001
n, k = map(int, input().split())
array = [0]*MAX #방문여부(0인지 아닌지) 겸 최단시간 저장 용도
print(bfs(n))
