import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
erase = int(input())

def dfs(erase, parent):
    parent[erase] = -2
    for i in range(n):
        if parent[i] == erase:
            dfs(i, parent)

dfs(erase, parent)

count = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        count += 1
print(count)

