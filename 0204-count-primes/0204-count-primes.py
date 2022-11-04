class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [True]*(n)
        limit = math.floor(math.sqrt(n))
        primes[0] = False
        primes[1] = False
        for i in range(2, limit+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
                
        count = 0
        for val in primes:
            if val == True:
                count += 1
        
        return count