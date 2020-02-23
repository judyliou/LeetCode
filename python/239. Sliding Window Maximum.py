from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        rtn = []
        for i, n in enumerate(nums):
            # keep the largest one
            while d and n > nums[d[-1]]:
                d.pop()
            d.append(i)
            
            # pop the one that is not in the window
            if d[0] == i-k:
                d.popleft()
                
            # output the maximum
            if i >= k-1:
                rtn.append(nums[d[0]])          
        return rtn
