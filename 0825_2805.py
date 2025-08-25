'''
나무 M미터 가져갈거임!
높이 H
나무의 수 N
'''
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    tree_heights = list(map(int, input().split()))

    start = 0
    end = max(tree_heights)
    result = 0

    while start <= end:
        mid = (start+end) // 2
        total_wood = 0

        for height in tree_heights:
            if height > mid:
                total_wood += height - mid
        
        if total_wood >= m: #원하는 만큼의 목재를 얻음
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)

solve()