'''
n개의 좌표
-10, -9, 2, 4, 4
0,  1,  2, 3, 3
'''
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

sorted_unique_x = sorted(list(set(x))) #set은 중복 제거

rank = {value: index for index, value in enumerate(sorted_unique_x)}
#enumerate는 인덱스와 원소로 이루어진 튜플 반환

result = [rank[value] for value in x]
#rank[value]: 딕셔너리 값 반환

print(*result)
