s = input()
reverse_s = s[::-1]

for i in range(len(s)):
    if s[i:] == reverse_s[0:len(s)-i]:
        print(len(s)+i)
        break




