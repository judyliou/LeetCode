class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [0]:
            return True
        
        zero_pos = len(nums) 
        zero = False
        for i in range(len(nums)-1, -1, -1):
            if not zero:
                if nums[i] == 0:
                    zero_pos = i
                    zero = True
            else:
                if nums[i] >  zero_pos - i or (nums[i] == zero_pos - i and zero_pos == len(nums)-1):
                    zero = False
        return (not zero)
                
            
