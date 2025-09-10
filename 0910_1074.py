import sys
input = sys.stdin.readline

n, r, c = map(int, input().split()) #r행c열
result = 0

while n != 0:
    n -= 1
    #2사분면
    if r<2**n and c<2**n:
        result += (2**n)*(2**n)*0
    #1사분면
    elif r<2**n and c>=2**n:
        result += (2**n)*(2**n)*1
        c -= 2**n
    #3사분면
    elif r>=2**n and c<2**n:
        result += (2**n)*(2**n)*2
        r -= 2**n
    #4사분면
    else:
        result += (2**n)*(2**n)*3
        r -= 2**n
        c -= 2**n

print(result)
