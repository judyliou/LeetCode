from collections import deque

# Solution 1: iterative with 2 queues
def isSymmetric(self, root):
    if root == None:   # base case
        return True
        
    left = deque([root.left])
    right = deque([root.right])
    while len(left) > 0 and len(right) > 0:
        l, r = left.popleft(), right.popleft()
        if r == None and l == None:
            continue
        elif r == None or l == None:
            return False
        elif r.val != l.val:
            return False
        left.extend([l.left, l.right])
        right.extend([r.right, r.left])

    if len(left) > 0 or len(right) > 0:  # check whether both queue is empty
        return False
    else:
        return True

# Solution 2: iterative with 1 queue
def isSymmetric(self, root):
    q = deque([root, root])
    while len(q) > 0:
        l, r = q.popleft(), q.popleft()
        if r == None and l == None:
            continue
        elif r == None or l == None:
            return False
        elif r.val != l.val:
            return False
        q.extend([l.left, r.right, l.right, r.left])
    return True
    
    
    from collections import deque

# Solution3: recursive
class Solution(object):
    def isSymmetric(self, root):
        if root == None: return True
        return self.isMirror(root.left, root.right)    
       
    def isMirror(self, l, r):
        if l == None and r == None:
            return True
        elif l == None or r == None:
            return False
        else:
            return (l.val == r.val) \
                and self.isMirror(l.left, r.right) \
                and self.isMirror(l.right, r.left)
