class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ''
        while n > 0:
            n -= 1
            cur = n % 26 
            title = (chr(cur+65)) + title
            n //= 26     
 
        return title
