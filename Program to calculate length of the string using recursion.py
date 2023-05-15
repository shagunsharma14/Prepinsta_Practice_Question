def strlength(s):
    if s=="":
        return 0
    return 1+strlength(s[1:])

s = 'abcd'
print(strlength(s))