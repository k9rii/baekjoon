import sys
input = sys.stdin.readline

left_stack = list(input().strip())
right_stack = []

m = int(input())
for _ in range(m):
    command = input().strip().split()
    
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

result = left_stack + right_stack[::-1]
print(''.join(result))

'''
L: 커서 왼쪽으로
D: 커서 오른쪽으로
B: 커서 왼쪽문자 삭제
P $: $라는 문자 커서 왼쪽에 추가
'''