'''
666

1666 2666 3666 4666 5666 
6660 6661 6662 6663 6664 6665 6666 
7666 8666 9666

10666 11666 12666 13666 14666 15666
16660 16661 16662 16663 16664 16665 16666
17666 18666 19666
'''

import sys
input = sys.stdin.readline

n = int(input())
count_n = 0
result = 666

while True:
    if '666' in str(result):
        count_n += 1

    if count_n == n:
        break

    result += 1

print(result)


