class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += [n + [i] for n in res]
        return res
