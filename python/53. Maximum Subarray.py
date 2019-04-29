# Solution 1: DP
class Solution(object):
    def maxSubArray(self, nums):
        Max = pre = nums[0]

        for i in range(1, len(nums)):
            if pre > 0:
                pre = pre + nums[i]
            else:
                pre = nums[i]
            
            if pre > Max:
                Max = pre  
        return Max

# Solution 2: Divide and Conquer
class Solution(object):
    def maxSubArrayDC(self, nums, l, r):    
        if l > r:
            return -2147483647
        m = (l + r) / 2

        left_max = left_sum = 0
        for i in range(m - 1, l - 1, -1):
            left_sum += nums[i]
            left_max = max(left_sum, left_max)

        right_max = right_sum = 0
        for i in range(m + 1, r + 1):
            right_sum += nums[i]
            right_max = max(right_sum, right_max)

        l_ans = self.maxSubArrayDC(nums, l, m - 1)
        r_ans = self.maxSubArrayDC(nums, m + 1, r)
        return max(left_max + nums[m] + right_max, l_ans, r_ans)

    def maxSubArray(self, nums):
        return self.maxSubArrayDC(nums, 0, len(nums) - 1)
