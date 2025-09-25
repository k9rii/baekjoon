import sys
input = sys.stdin.readline

n = int(input()) #4
road = list(map(int, input().split())) #231
money = list(map(int, input().split())) #5241

result = road[0] * money[0]
min_money = money[0]

def sol():
    global result #이거 전역선언 안해서 오류났었음!!
    global min_money
    for i in range(1, n-1): #1,2
        if money[i] <= min_money:
            result += money[i]*road[i]
            min_money = money[i]
        else:
            result += min_money*road[i]

sol()
print(result)



