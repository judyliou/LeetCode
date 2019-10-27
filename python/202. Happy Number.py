class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while n not in record:
            record.append(n)
            n = sum(int(d)**2 for d in str(n)) 
        return n == 1
