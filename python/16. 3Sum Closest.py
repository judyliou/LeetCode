# Time Complexity: O(n^2)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sum(nums[:3])

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif abs(s - target) < abs(closest - target):
                    closest = s

                if s < target: 
                    l += 1
                else: 
                    r -= 1
        return closest
