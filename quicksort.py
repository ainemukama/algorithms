def quicksort(arr):
    n = len(arr)
    if n == 0:
        return list()
    piv = n/2
    smaller = [x for x in arr if x < arr[piv]]
    bigger = [x for x in arr if x > arr[piv]]
    same = [x for x in arr if x == arr[piv]]
    return quicksort(smaller) + same + quicksort(bigger)

arr = [4, 1, 2, 5, 3, 8, 9, 6, 1]
print quicksort(arr)
