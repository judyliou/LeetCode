# Solution 1
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
    

# Solution 2
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        arr = [1] * (n+1)
        arr[0] = arr[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if arr[i] == 1:  # if is 0, it's multiples must become 0 already as well
                for j in range(i*i, n+1, i):  # start from i*i because i*(i-1), i*(i-2),etc. have already be checked by (i-1), (i-2)
                    arr[j] = 0
        arr[n] = 0
        return sum(arr)
