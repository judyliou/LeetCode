# Solution 1: Dynamic Programming -- O(n)
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2: 
            return 2
        else:
            pre1 = 1
            pre2 = 2
            for i in range(n-2):
                now = pre1 + pre2
                pre1 = pre2
                pre2 = now
            return now

# Solution 2: O(logn)
class Solution(object):
    def mul(self, a, b):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                result[i][j] = a[i][0] * b[j][0] + a[i][1] * b[1][j]
        return result

    def climbStairs(self, n):        
        # fn = fn-1 * A = f1 * A^(n-1) 
        A = [[1, 1], [1, 0]]
        f1 = [[1, 1], [1, 0]]
        n -= 1
        
        while n > 0:
            if (n & 1) == 1:
                f1 = self.mul(f1, A)
            A = self.mul(A, A)
            n = n >> 1
        return f1[0][0]
        
