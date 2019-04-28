#Solution 1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        m = len(needle)
        n = len(haystack)
        
        f = [0] * m
        
        # failure function
        i = 1
        j = 0
        while i < m:
            if needle[i] == needle[j]:
                f[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = f[j-1]
            else:
                i += 1
                
        # KMP matching
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                if j == m - 1:
                    return i - m + 1
                i += 1
                j += 1
            elif f[j] > 1:
                j = 0
            elif j > 0:  # f[j] = 0 or 1
                j = f[j-1]
            else:
                i += 1 
        return -1
        
# Solution 2
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
                
                
