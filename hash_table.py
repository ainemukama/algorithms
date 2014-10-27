from collections import defaultdict

class HashTable():

    def __init__(self):
        self.table = defaultdict(list)

    def add(self, item):
        self.table[item[0]].append(item)

    def describe(self):
        for k, v in self.table.iteritems():
            print k, v

ht = HashTable()
ht.add('dog')
ht.add('cat')
ht.add('caterpillar')
ht.describe()
