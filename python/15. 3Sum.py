# Time: O(nlogn + n^2) ~= O(n^2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # O(nlogn)
        sol = []
        for i in range(len(nums)-2):
            if nums[i] > 0:  # sum of three positive numbers always greater than 0
                break 
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    # check other triplets with nums[i]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return sol
