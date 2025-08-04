'''
버블 정렬 사용시, 시간초과
병합 정렬 O(nlogn) 활용
병합 정렬 과정에서 숫자가 이동한 만큼이 버블 정렬의 swap 수와 동일
'''

import sys
input = sys.stdin.readline
result = 0

def merge_sort(s, e):
    global result
    if e-s < 1: return #구간 길이가 1이하면 종료
    m = int(s + (e-s)/2) #중간지점 m
    merge_sort(s, m) #재귀분할
    merge_sort(m+1, e) #재귀분할

    for i in range(s, e+1): 
        tmp[i] = a[i] #원본배열a의 현재 구간을 임시배열tmp에 복사

    k = s #병합 결과 저장 위치
    index1 = s #왼쪽 절반 순회
    index2 = m+1 #오른쪽 절반 순회
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]: #swap 발생
            a[k] = tmp[index2]
            result = result + (index2 - k) #오른쪽 값이 앞으로 오는 횟수: index2-k
            k += 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        a[k] = tmp[index1]
        k += 1
        index1 += 1
        
    while index2 <= e:
        a[k] = tmp[index2]
        k += 1
        index2 += 1

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
tmp = [0] * int(n+1)
merge_sort(1, n)
print(result)
