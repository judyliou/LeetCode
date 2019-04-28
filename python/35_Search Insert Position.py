class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
     
        left = 0
        right = len(nums) - 1
        
        # compare left or right
        while left < right:
            n = int((left + right) / 2)
            
            if nums[n] == target:
                return n
            elif nums[n] > target:
                right = n - 1
            else:
                left = n + 1
        return left if target <= nums[left] else left + 1
