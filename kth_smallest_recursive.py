def kth_smallest(arr, k):
    n = len(arr)
    if k < 0 or k >= n:
        return None
    piv = n/2
    smaller = list()
    bigger = list()
    for i, x in enumerate(arr):
        if i != piv:
            if x < arr[piv]:
                smaller.append(x)
            else:
                bigger.append(x)

    if len(smaller) == k:
        return arr[piv]
    elif len(smaller) < k:
        return kth_smallest(bigger, k - len(smaller) - 1)
    else:
        return kth_smallest(smaller, k)

arr = [1, 3, 5, 7, 7, 7, 9]
for i in range(-1, len(arr)+1):
    print i, kth_smallest(arr, i)
