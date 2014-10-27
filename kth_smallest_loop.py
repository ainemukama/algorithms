def kth_smallest(arr, k):
    n = len(arr)
    a = 0
    b = n
    while a < b:
        piv = a
        for i in range(a, b):
            if arr[piv] > arr[i]:
                arr[i], arr[piv] = arr[piv], arr[i]
                piv = i
        if piv == k:
            return arr[piv]
        elif piv < k:
            a = piv+1
        else:
            b = piv-1

arr = [9, 3, 5, 6, 1, 3, 3]
print arr
for i in range(-1, len(arr)+1):
    print i, kth_smallest(arr, i)
