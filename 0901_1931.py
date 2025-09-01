import sys
input = sys.stdin.readline

n = int(input())
A = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int, input().split())
    A[i][0] = end
    A[i][1] = start

A.sort() #종료시각 기준으로 정렬. 종료 시각이 같으면 시작시각 기준 정렬
count = 0
end = -1

for i in range(n):
    if A[i][1] >= end: #앞 회의의 종료 시각보다 시작 시각이 늦은 회의가 나온 경우
        end = A[i][0] #현재 회의 종료 시각으로 종료 시각 업데이트
        count += 1 #진행할 수 있는 회의 수 증가
print(count)
