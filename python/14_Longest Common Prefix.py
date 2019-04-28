class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs or "" in strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        # examine through column
        for i in range(len(strs[0])): # column number
            c = strs[0][i]
            for j in range(1, len(strs)):  # row number
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]
