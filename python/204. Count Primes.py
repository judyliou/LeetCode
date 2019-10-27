class Solution(object):
    def generate_prime(self, n):
        primes = [1] * (n)
        root = int(n**(0.5))
        for i in range(2, root+1):
            for j in range(i*2, n, i):
                primes[j] = 0
        return primes
       
    def countPrimes(self, n):
        if n < 2: 
            return 0
        primes = self.generate_prime(n)
        return sum(primes[2:])
    
