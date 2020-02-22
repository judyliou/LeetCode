from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        pre = [root]
        res = []
        while len(pre) != 0:
            val = []
            cur = []
            for i in pre:
                val.append(i.val)
                if i.left: 
                    cur.append(i.left)
                if i.right: 
                    cur.append(i.right)
            res.append(val)
            pre = cur
        return res
