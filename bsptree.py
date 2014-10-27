import sys

class Node(object):

    def __init__(self, a, b=None):
        if isinstance(a, int):
            self.value = a
            self.left = None
            self.right = None
        elif isinstance(a, Node):
            self.value = None
            self.left = a
            self.right = b
        else:
            print 'bad type, exiting'
            sys.exit(1)

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return '[%s %s]' % (self.left, self.right)

    def bitwise_and(self, tree2):
        if self.value == 0:
            return self
        elif tree2.value == 0:
            return tree2
        elif self.value == 1:
            return tree2
        elif tree2.value == 1:
            return self
        else:
            left = self.left.bitwise_and(tree2.left)
            right = self.right.bitwise_and(tree2.right)
            return Node(left, right)

tree1 = Node(Node(Node(0), Node(1)), Node(Node(1), Node(0)))
tree2 = Node(0)
tree3 = tree2.bitwise_and(tree1)

print tree1
print tree2
print tree3
