#swap이 일어나지 않은 루프 몇번인지 알아내기 문제  

import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append((int(input()), i))

max = 0
sorted_a = sorted(a)

for i in range(n):
    if max < sorted_a[i][1] - i:
        max = sorted_a[i][1] - i
print(max+1)