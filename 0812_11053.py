import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int, input().split()))

dp = [1] * a #가장 긴 증가하는 부분 수열의 길이 저장
for i in range(1, a):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
