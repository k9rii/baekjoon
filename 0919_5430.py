import sys
input = sys.stdin.readline
from collections import deque

def solution():
    p = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n > 0:
        arr = arr_str[1:-1].split(',')
        dq = deque(arr)
    else:
        dq = deque()

    rev = 0
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            rev += 1
        elif cmd == 'D':
            if not dq:
                error_flag = True
                break
            if rev % 2 == 0:
                dq.popleft()
            else:
                dq.pop()

    if error_flag:
        print("error")
    else:
        if rev % 2 != 0:
            dq.reverse()
        print("[" + ",".join(dq) + "]")

T = int(input())
for _ in range(T):
    solution()

    