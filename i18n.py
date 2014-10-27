#!/usr/bin/env python
from collections import defaultdict

def abbreviate(words):
    abbrvs = defaultdict(list)
    for w in words:
        abbr = w[0] + str(len(w)-2) + w[-1]
        abbrvs[abbr].append(w[1:])

    all_abbrvs = list()
    for k in abbrvs:
        if len(abbrvs[k]) > 1:
            all_abbrvs.extend([k[0] + w for w in abbreviate(abbrvs[k])])
        else:
            all_abbrvs.append(k)

    return all_abbrvs

if __name__=='__main__':
    words = ['internationalization', 'abxxxxxxxz', 'acdxxxxxxz', 'acxxxxxxxz']
    for w in abbreviate(words):
        print w

