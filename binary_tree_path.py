class Node(object):

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        if left is not None:
            self.left.parent = self
        if right is not None:
            self.right.parent = self

    def path_to(self, node):
        anc = node.ancestors()
        inode = self
        while inode is not None:
            if inode in anc:
                i = anc.index(inode)
                for jnode in anc[i:]:
                    print jnode.key
            else:
                print inode.key
            inode = inode.parent

    def ancestors(self):
        """includes itself"""
        if self.parent is None:
            return [self]
        else:
            return self.parent.ancestors() + [self]

node3 = Node(3)
node4 = Node(4)
tree = Node(0, Node(1, node3, Node(5)), Node(2, Node(6, left=Node(7)), node4))

node3.path_to(node4)
