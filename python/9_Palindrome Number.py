# Solution 1
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        rev, x_copy = 0, x
        while x:
            end = x % 10
            rev = rev * 10 + end
            x //= 10
        if rev == x_copy:
            return True
        else:
            return False
            
 
# Solution 2 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        rev = 0
        while x and rev < x:
            end = x % 10
            rev = rev * 10 + end
            x //= 10
        return x == rev or x == rev // 10
            

# Solution 3
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        else:
            return False
