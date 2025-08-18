n, m = map(int, input().split()) #레슨 n개, 블루레이 m개
A = list(map(int, input().split())) #기타레슨 데이터 저장 리스트
start = 0 #시작 인덱스
end = 0 #종료 인덱스

for i in A:
    if start < i:
        start = i #시작 인덱스 저장(A리스트 중 최댓값)
    end += i #A리스트의 총합

while start <= end: #이진탐색!!
    middle = int((start+end)/2) #중간인덱스
    sum = 0 #레슨 합
    count = 0 #현재 사용한 블루레이 개수 <= m

    for i in range(n):
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
        #sum에 레슨시간을 계속 더하다가 middle을 초과하면 count 1증가, sum 0초기화하여 새로운 블루레이 사용

    if sum != 0:
        count += 1

    if count > m:
        start = middle + 1
    else:
        end = middle - 1

print(start)

