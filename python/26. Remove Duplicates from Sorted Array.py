# Solution 1
def removeDuplicates(self, nums):
    if len(nums) == 0:
        return 0
    # two pointers
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
   
# Solution 2:
def removeDuplicates(self, nums):
    if len(nums) == 0:
        return 0
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

# Solution 3: remove from back
def removeDuplicates(self, nums):
    if nums == None:
        return 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]
    return len(nums)
                
