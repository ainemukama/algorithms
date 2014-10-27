class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def exists(self, x):
        if self.value == x:
            return True

        if self.left is not None:
            in_left = self.left.exists(x)
        else:
            in_left = False
        if self.right is not None:
            in_right = self.right.exists(x)
        else:
            in_right = False
        return in_left or in_right


bst = Node(5, Node(3, Node(2), Node(4)), Node(7, Node(5), None))
print bst.exists(4)
print bst.exists(1)
