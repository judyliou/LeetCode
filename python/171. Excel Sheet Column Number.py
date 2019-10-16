# Solution 1: while
class Solution(object):
    def titleToNumber(self, s):
        num = 0
        digit = 0
        while len(s) > 0:
            num += (ord(s[-1]) - ord('A') + 1) * pow(26, digit)
            s = s[:-1]
            digit += 1
        return num
        
 # Solution 2: for-loop       
class Solution(object):
    def titleToNumber(self, s):
        num = 0
        for i in range(len(s)):
            num += (ord(s[-(i+1)]) - 64) * 26**i
        return num
