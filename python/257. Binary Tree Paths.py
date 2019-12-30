# Recursion
class Solution(object):
    def binaryTreePaths(self, root):
        curPath = ""
        allPath = []
        return self.findPath(root, curPath, allPath)
        
    def findPath(self, root, curPath, allPath):
        if root == None:
            return allPath
        if root.left == None and root.right == None:
            path = curPath + str(root.val)
            allPath.append(path)
            return allPath
        
        curPath += str(root.val) + "->"
        allPath = self.findPath(root.left, curPath, allPath)
        allPath = self.findPath(root.right, curPath, allPath)
        return allPath
        
        
# Iteration
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        allPath = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if node.left == None and node.right == None:
                path += str(node.val)
                allPath.append(path)
            else:
                path += str(node.val) + '->'
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        return allPath
