class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I, V, X, L, C, D, M
        trans = {"I": 1, "V": 5, "X": 10, "L":50,\
                "C": 100, "D": 500, "M": 1000}
        
        last = trans[s[0]] # first number
        total = 0
        
        for i in range(1, len(s)):
            if trans[s[i]] > last:
                total -= last
            else:
                total += last
            last = trans[s[i]]
        
        total += trans[s[-1]]
        
        return total
