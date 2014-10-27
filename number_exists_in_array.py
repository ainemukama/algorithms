def quicksort(arr):
    n = len(arr)
    if n > 0:
        a = list()
        b = list()
        c = list()
        piv = n/2
        for x in arr:
            if x == arr[piv]:
                b.append(x)
            elif x < arr[piv]:
                a.append(x)
            elif x > arr[piv]:
                c.append(x)
        arr = quicksort(a) + b + quicksort(c)
    return arr

class BST(object):

    def __init__(self, arr):
        """assumes array is sorted"""
        n = len(arr)
        piv = n/2
        self.value = arr[piv]
        if n == 1:
            self.left = self.right = None
        elif n == 2:
            self.left = BST(arr[:1])
            self.right = None
        else:
            self.left = BST(arr[:piv])
            self.right = BST(arr[piv+1:])

def number_exists(arr, x):
    arr = quicksort(arr)
    tree = BST(arr)
    while tree:
        if tree.value == x:
            return True
        elif tree.value < x:
            tree = tree.right
        elif tree.value > x:
            tree = tree.left
    return False


def number_exists(arr, n):
    i = 0
    j = len(arr)-1
    while i < j - 1:
        piv = (i+j)/2
        if arr[piv] == n:
            return True
        elif arr[piv] < n:
            i = piv
        else:
            j = piv
    return arr[i] == n or arr[j] == n

arr = [1, 3, 4, 6, 9, 11]
print number_exists(arr, 9)
print number_exists(arr, 8)
arr = [6, 9, 3, 6, 6, 8, 8, 0]

arr_sorted = quicksort(arr)
print arr
print arr_sorted

for i in range(10):
    print i, number_exists(arr, i)
