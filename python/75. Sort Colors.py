# Solution 1: Counting Sort
def sortColors(nums):
    count = [0] * 3
    for i in nums:
        count[i] += 1

    i = 0    
    for num in range(3):
        for t in range(count[num]):
            nums[i] = num
            i += 1

    
# Solution 2: two pointers
def sortColors(self, nums):
    left, right = 0, len(nums)-1
    cur = 0
    while cur <= right:
        if nums[cur] == 0:
            nums[left], nums[cur] = nums[cur], nums[left]
            left += 1
            cur += 1
        elif nums[cur] == 1:
            cur += 1
        else:
            nums[right], nums[cur] = nums[cur], nums[right]
            right -= 1
