import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0 #합이 s인 부분수열의 개수 저장용 변수
ans = [] #현재 만들어지고 있는 부분수열 저장용 리스트

def sol(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1
    for i in range(start, n):
        ans.append(num[i])
        sol(i+1)
        ans.pop()

sol(0)
print(cnt)


