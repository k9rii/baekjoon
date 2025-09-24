import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort() #사전순 출력을 위해
#n개의 자연수 중에서 m개를 고른 수열

arr = []
visited = [False]*n

def sol():
    if len(arr) == m:
        print(*arr)
        return 
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(num[i])
            sol()
            arr.pop()
            visited[i] = False

sol()
