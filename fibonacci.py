def fibonacci_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n):
            c = a + b
            a, b = b, c
    return c
        
for i in range(10):
    print fibonacci_iterative(i)
