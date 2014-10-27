def atoi(s):
    if s[0] == '-':
        return -reduce(lambda x,y: 10*int(x) + int(y), s[1:])
    else:
        return reduce(lambda x,y: 10*int(x) + int(y), s)

print atoi("123")
print atoi("-123")
print atoi("0")
