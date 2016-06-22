def fizzbuzz(n, a=3, b=4):
    for i in range(n):
        if i % (a*b) == 0:
            print i, 'fizzbuzz'
        elif i % a == 0:
            print i, 'fizz'
        elif i % b == 0:
            print i, 'buzz'
        else:
            print i

fizzbuzz(40)
