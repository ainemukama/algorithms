from collections import defaultdict

def has_common_chars(s1, s2):
    chars = defaultdict(int)
    i1 = 0
    n1 = len(s1)
    for c2 in s2:
        while chars[c2] == 0:
            if i1 == n1:
                return False
            chars[s1[i1]] += 1
            i1 += 1
        chars[c2] -= 1
    return True
    
s1 = 'the quick brown fox jumped over the lazy dog'

print has_common_chars(s1, 'z')
print has_common_chars(s1, 'zq')
print has_common_chars(s1, 'gq')
print has_common_chars(s1, 'zz')
print has_common_chars(s1, 'dog')
