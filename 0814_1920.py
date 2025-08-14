import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
#set로 저장하면 중복 저장 막음!!

m = int(input())
find = list(map(int, input().split()))

for i in range(m):
    if find[i] in arr:
        print(1)
    else:
        print(0)
