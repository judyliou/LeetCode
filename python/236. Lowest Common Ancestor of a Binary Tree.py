class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if root == p or root == q:
            return root
            
        left = self.lowestCommonAncestor(root.left, p, q)
        if left != p and left != q and left != None: # Already found 
            return left
        
        right = self.lowestCommonAncestor(root.right, p, q)
        if right != p and right != q and right != None: # Already found 
            return right
        
        if left != None and right != None: # p and q are in different side
            return root
        else:
            return left if left else right
            
            
# If not guarantee p and q in the tree
class Result(object):
    def __init__(self, node, isValid):
        self.node = node
        self.isValid = isValid
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        result = self.findAnc(root, p, q)
        if result.isValid:
            return result.node
        else:
            return None
        
    def findAnc(self, root, p, q):
        if root == None:
            return Result(None, False)
            
        leftR = self.findAnc(root.left, p, q)
        if leftR.isValid == True:   # Already found
            return leftR
            
        rightR = self.findAnc(root.right, p, q)
        if rightR.isValid == True:  # Already found
            return rightR
        
        if root == p or root == q:
            isValid = rightR.node != None or leftR.node != None   # True if p is in q's subtree
            return Result(root, isValid)
        elif leftR.node != None and rightR.node != None:          # p and q are in different side
            return Result(root, True)
        else:
            # both None --> return None; one is not None --> return the node
            return Result(leftR.node if leftR.node != None else rightR.node, False)
