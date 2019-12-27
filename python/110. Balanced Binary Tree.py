# Solution 1: time complexity-O(NlogN)
class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, node):
        if node == None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        
# Solution 2: time complexity-O(N)
MIN = -100
class Solution(object):
    def isBalanced(self, root):
        return self.checkHeight(root) != MIN
        
    def checkHeight(self, node):
        if node == None:
            return 0
        left = self.checkHeight(node.left)
        if left == MIN:
            return MIN
        
        right = self.checkHeight(node.right)
        if right == MIN:
            return MIN
        
        if abs(left - right) > 1:
            return MIN
        else:
            return max(self.checkHeight(node.left), self.checkHeight(node.right)) + 1
