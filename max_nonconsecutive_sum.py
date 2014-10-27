from collections import defaultdict

def max_nonconsecutive_sum(arr):
    n = len(arr)
    max_sum = defaultdict(int)
    for i in range(n):
        max_sum[i] = max(max_sum[i-1], arr[i] + max_sum[i-2])
    return max_sum[n-1]

print max_nonconsecutive_sum([3, 2, 7, 1])
print max_nonconsecutive_sum([6, 2, 1, 4])
print max_nonconsecutive_sum([8, 9, 5, 1])
print max_nonconsecutive_sum([29, 77, 16])
print max_nonconsecutive_sum([29, 44, 16])
