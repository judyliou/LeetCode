# time: O(2^n), space: O(2^n)
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        self.helper(n, n, '', ans)
        return ans
    
    def helper(self, left, right, path, ans):
        if left == 0 and right == 0:
            ans.append(path)
        else:
            if left > 0:
                self.helper(left-1, right, path+'(', ans)
            if right > 0 and left < right:
                self.helper(left, right-1, path+')', ans)
                
