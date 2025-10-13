import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input()) #행성 개수
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        dis1 = (x1-cx)**2 + (y1-cy)**2
        dis2 = (x2-cx)**2 + (y2-cy)**2
        cr = r**2

        if cr > dis1 and cr > dis2:
            continue
        elif cr > dis1:
            count += 1
        elif cr > dis2:
            count += 1
            
    print(count)
        

