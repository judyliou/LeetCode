# Sol 1: time complexity O(n), memory complexity O(n)
def missingNumber(self, nums):  
    ref = [i for i in range(len(nums)+1)]
    for i in nums:
        ref.remove(i)
    return ref[0]
    
# Sol 2: time complexity O(n), memory complexity O(1)
def missingNumber(self, nums):     
    sum = 0
    for i in nums:
        sum += i
    total = (1 + len(nums)) * len(nums) / 2
    return total - sum
