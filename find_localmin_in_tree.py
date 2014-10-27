class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find_local_min(self):
        if self.left and self.value > self.left.value:
            return self.left.find_local_min()
        elif self.right and self.value > self.right.value:
            return self.right.find_local_min()
        else:
            return self.value

tree = Node(7, Node(8), Node(3, None, Node(5)))
print tree.find_local_min()
