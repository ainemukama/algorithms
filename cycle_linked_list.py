class Node(object):

    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    def cycle_exists(self):
        slow = self
        fast = self.next
        while slow is not None and fast is not None and fast.next is not None:
            if fast.next is slow or fast is slow:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False

node4 = Node(4)
node1 = Node(1, Node(2, Node(3, node4)))
node0 = Node(0, node1)
#node4.next = node1

print node0.cycle_exists()
