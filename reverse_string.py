def reverse_string(s):
    n = len(s)
    s = list(s)
    for i in range(n/2):
        s[i], s[n-i-1] = s[n-i-1], s[i]
    return ''.join(s)

print reverse_string('hello world')
