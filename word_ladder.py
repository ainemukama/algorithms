class Node(object):

    def __init__(self, value):
        self.value = value
        self.neighbors = list()

    def add_neighbor(self, node):
        self.neighbors.append(node)

cat = Node('cat')
dog = Node('dog')
dot = Node('dot')
cot = Node('cot')
cap = Node('cap')
hat = Node('hat')
hot = Node('hot')

cat.add_neighbor(hat)
cat.add_neighbor(cot)
cat.add_neighbor(cap)
dog.add_neighbor(dot)
dot.add_neighbor(cot)
dot.add_neighbor(hot)
hot.add_neighbor(hat)
