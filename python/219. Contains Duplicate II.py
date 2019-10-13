# Time: O(n), Space: O(n)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, n in enumerate(nums):
            if n in dict and i - dict[n] <= k:
                return True
            else:
                dict[n] = i
        return False
                
