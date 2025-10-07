import sys
input = sys.stdin.readline

n, l = map(int, input().split())
#합이 n이면서 길이가 적어도 l인 가장 짧은 연속된 음이 아닌 정수 리스트

for i in range(l, 101):
    x = n/i - (i+1)/2
    if int(x) == x: #x가 정수
        x = int(x)
        if x >= -1:
            for j in range(x+1, x+i+1):
                print(j, end=' ')
            break

else:
    print(-1)