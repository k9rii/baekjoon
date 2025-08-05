'''
한수
1~n
1 2 3 4 5 6 7 8 9 
10 11 12 13 14 15 16 17 18 19 20
1~99까지는 모두 한수
111
123
135
147
159

'''

n = int(input())
result = 0

for i in range(1, n+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        result += 1
    elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
        result += 1
print(result)