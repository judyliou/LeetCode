# Solution 1
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        temp = []
        d = {'(': ')', '{': '}', '[': ']'}
        
        if not s:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            for i in s:
                if i in d:
                    temp.append(i)
                else:
                    if len(temp) != 0 and d[temp.pop()] == i:
                        continue
                    else:
                        return False
            
            return len(temp) == 0
                    

# Solution 2
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('()', "").replace('[]', "").replace('{}', "")
            
        return len(s) == 0
