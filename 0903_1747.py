import math

n = int(input())
A = [0]*(10000001) #소수 리스트

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i): #배수 지우기
        A[j] = 0

def isPalindrome(target):
    temp = list(str(target)) #소수를 리스트형태로 변환한 후, 
    s = 0 #양끝 투포인터 활용해서 서로 같은지(펠린드롬수인지) 확인
    e = len(temp) - 1
    while (s<e):
        if temp[s] != temp[e]:
            return False
        s+=1
        e-=1
    return True

i = n
while True:
    if A[i] != 0: #소수이고
        result = A[i]
        if (isPalindrome(result)): #펠린드롬수면 출력
            print(result)
            break
    i += 1
