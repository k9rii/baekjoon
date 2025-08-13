from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    user = list(input().split())

    if user[0] == "push":
        stack.append(int(user[1]))

    elif user[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif user[0] == "size":
        print(len(stack))

    elif user[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif user[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)