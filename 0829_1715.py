from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    data = int(input())
    pq.put(data)

if n == 1:
    print(0)
    exit()

sum = 0

while pq.qsize() > 1:
    data1 = pq.get() #2개 카드 묶음을 큐에서 뽑음(꺼내기))
    data2 = pq.get()
    temp = data1 + data2 
    sum += temp #2개 카드 합치는 데 필요한 비교 횟수를 결과값에 저장
    pq.put(temp) #2개 카드 묶음의 합을 우선순위 큐에 다시 넣음
print(sum)
