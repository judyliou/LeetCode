# Recursive
class Solution(object):
    def hasPathSum(self, root, sum):
        return self.findPath(root, sum)
        
    def findPath(self, root, remain):
        if root == None:
            return False
        remain -= root.val
        if remain == 0 and root.left == None and root.right == None:
            return True
        else:
            return self.findPath(root.right, remain) or self.findPath(root.left, remain)


# Iterative
from collections import deque
class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        q = deque([(root, sum-root.val)])
        while q:
            node, remain = q.popleft()
            if remain == 0 and node.left == None and node.right == None:
                return True
            else:
                if node.left != None:
                    q.append((node.left, remain - node.left.val))
                if node.right != None:
                    q.append((node.right, remain - node.right.val))
        return False
