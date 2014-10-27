class Node(object):

    def __init__(self, key):
        self.key = key
        self.connected_nodes = set()

    def is_connected(self, node):
        if node in self.connected_nodes:
            return True
        else:
            self.connected_nodes.add(node)
            node.connected_nodes.add(self)
            for cnode in self.connected_nodes:
                cnode.connected_nodes.add(node)
                node.connected_nodes.add(cnode)
            for cnode in node.connected_nodes:
                cnode.connected_nodes.add(self)
                self.connected_nodes.add(cnode)
            return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

print '1 2', node1.is_connected(node2)
print '2 3', node2.is_connected(node3)
print '1 3', node1.is_connected(node3)
print '1 4', node1.is_connected(node4)
print '3 5', node3.is_connected(node5)
print '4 5', node4.is_connected(node5)
