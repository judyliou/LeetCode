# Solution 1: Time complexity: O(n), Space complexity : O(n)
class Solution(object):
    def singleNumber(self, nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d.keys()[d.values().index(1)]

# Solution 2: Time complexity: O(n), Space complexity : O(n) [`set` needs space n]
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

# Solution 3: Time complexity: O(n), Space complexity : O(1)
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
