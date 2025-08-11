import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

#2 -> 9
#5 -> 6
#n-k+1까지
result = []
result.append(sum(arr[:k]))

for i in range(n-k):
    result.append(result[i] - arr[i] + arr[k+i])
print(max(result))
