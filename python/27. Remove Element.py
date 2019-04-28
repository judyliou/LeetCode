# Solution 1
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l
        
        
# Solution 2
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
                

# Solution 3
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in set(nums):
            nums.remove(val)
        return len(nums)
