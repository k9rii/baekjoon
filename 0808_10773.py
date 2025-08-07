k = int(input())
a = []
for _ in range(k):
    n = int(input())
    if n != 0:
        a.append(n)
    else:
        a.pop()

result = 0
for i in a:
    result += i
print(result)
