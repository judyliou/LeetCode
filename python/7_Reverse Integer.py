# Solution 1
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        new_x, x = 0, abs(x)
        while x:
            new_x = 10 * new_x + x % 10
            x /= 10
        new_x *= flag 
        return new_x if new_x < 2147483648 and new_x >= -2147483648 else 0

    
# Soluiton 2
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(str(x)[::-1]) if x > 0 else -int(str(-x)[::-1])
        return x if x < 2147483648 and x >= -2147483648 else 0
