from numpy.random import randint

def shuffle(arr):
    n = len(arr)
    for i in range(n):
        j = randint(i, n)
        arr[i], arr[j] = arr[j], arr[i]

for trial in range(10):
    arr = range(4)
    shuffle(arr)
    print arr
