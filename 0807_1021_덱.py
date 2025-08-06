from collections import deque
import sys
input = sys.stdin.readline
#n개의 원소를 가진 순환큐에서 m개의 원소 뽑아낼 때
#최소 회전 연산 횟수 계산

n, m = map(int, input().split())
targets = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)]) #1~n

count = 0
for i in targets:
    while True:
        if dq[0] == i: #dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2: #뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈 것보다 작을때는 왼쪽으로 움직여야 함!
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count += 1
            else: #뽑아내려는 수의 위치 인덱스가 dq의 길이 반으로 나눈것보다 클때는 오른쪽으로!
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)