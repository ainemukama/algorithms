from collections import defaultdict

class Sieve(object):
    
    def __init__(self, nmax):
        self.iscomp = defaultdict(bool)
        self.nmax = nmax
        for n in range(2, nmax):
            m = 2*n
            while m <= nmax:
                self.iscomp[m] = True
                m += n

    def isprime(self, n):
        if n < 2:
            return False
        else:
            return not self.iscomp[n]

    def find_all_primes(self, nmax):
        return [n for n in range(2, min(self.nmax, nmax)) if not self.iscomp[n]]

sieve = Sieve(100)

for i in range(0, 50):
    print i, sieve.isprime(i)

print sieve.find_all_primes(110)
