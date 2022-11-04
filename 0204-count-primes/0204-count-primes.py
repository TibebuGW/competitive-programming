class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [True]*(n)
        primes[0] = False
        primes[1] = False
        i = 2
        while i*i < n:
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
            i += 1
        count = 0
        for val in primes:
            if val == True:
                count += 1
        
        return count