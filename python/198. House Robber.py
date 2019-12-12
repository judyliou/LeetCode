def rob(self, nums):
    nums.insert(0, 0)
    if len(nums) <= 2:
        return nums.pop()
    for i in range(2, len(nums)):
        nums[i] = max(nums[i]+nums[i-2], nums[i-1])
    return nums.pop()
