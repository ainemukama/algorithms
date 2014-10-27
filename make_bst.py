class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "%s [%s %s]" % (self.value, self.left, self.right)

def make_bst_from_sorted(arr):
    n = len(arr)
    if n == 0:
        return None
    piv = n/2
    return Node(arr[piv], make_bst_from_sorted(arr[:piv]), make_bst_from_sorted(arr[piv+1:]))

arr = [4, 3, 2, 7, 5, 5]
arr_sorted = sorted(arr)
print make_bst_from_sorted(arr_sorted)
