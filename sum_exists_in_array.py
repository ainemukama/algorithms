def sum_exists(arr, S):
    y = sorted(arr)
    i = 0
    j = len(y)-1
    while i < j:
        temp_sum = y[i] + y[j]
        if temp_sum == S:
            return True
        elif temp_sum > S:
            j = j-1
        elif temp_sum < S:
            i = i+1
    return False

x = [9, 3, 0, 6, 1]
print sum_exists(x, 7)
print sum_exists(x, 4)
print sum_exists(x, 9)
print sum_exists(x, 17)
print sum_exists(x, 8)
print sum_exists(x, 5)
print sum_exists(x, 11)
print sum_exists(x, 2)
