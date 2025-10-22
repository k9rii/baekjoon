import sys
input = sys.stdin.readline

#AAAA, BB
user = input()
user = user.replace("XXXX", "AAAA")
user = user.replace("XX", "BB")

if 'X' in user:
    print(-1)
else:
    print(user)



