# Sol 1: sum every time after requesting
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])


# Sol 2: make a sum table first
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.sum = [0]
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            self.sum.append(t)

    def sumRange(self, i, j):
        return self.sum[j+1] - self.sum[i]
