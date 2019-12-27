# Solution 1: recursion
class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            
            
# Solution 2: iteration
from collections import deque
class Solution(object):
    def minDepth(self, root):
        visit = deque([(root, 1)])
        while len(visit) != 0:
            nextNode, curHeight = visit.popleft()
            if nextNode == None:
                continue
    
            if nextNode.left == None and nextNode.right == None:
                return curHeight
            
            visit.append([nextNode.left, curHeight + 1])
            visit.append([nextNode.right, curHeight + 1])
        return 0
        
