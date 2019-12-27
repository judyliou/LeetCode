# Iteration
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
 
# Recursion
class Solution(object): 
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
# If not a BST
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if self.cover(root, p) and self.cover(root, q): # make sure p and q are in the tree
            return self.LCA(root, p, q)
        else:
            return None
    
    def cover(self, root, target):
        if root == None:
            return False
        if root == target:
            return True
        return self.cover(root.left, target) or self.cover(root.right, target)
    
    def LCA(self, root, p, q):
        if root == p or root == q:
            return root
        pLeft = self.cover(root.left, p)
        qLeft = self.cover(root.left, q)
        if pLeft != qLeft: # p and q on different side
            return root
        else:
            childSide = root.left if pLeft else root.right
            return self.LCA(childSide, p, q)
