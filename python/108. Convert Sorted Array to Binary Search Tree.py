class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.buildTree(nums)
        return root
        
    def buildTree(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildTree(nums[:mid])
        node.right = self.buildTree(nums[mid+1:])
        return node
