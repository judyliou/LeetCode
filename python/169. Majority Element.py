# Solution 1: Count with dict
# Time Complexity: O(n), Space Complexity: O(n)
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = {}
    for i in nums:
        cnt[i] = cnt.get(i, 0) + 1
    for k, v in cnt.items():
        if v > len(nums) // 2:
            return k
    
    
# Solution 2: Sorting 
# Time Complexity: O(nlogn), Space Complexity: O(n)
def majorityElement(self, nums):
    nums.sort()
    return nums[len(nums)//2]
  
  
# Solution 3: Divide and Conquer
# Time Complexity: O(nlogn), Space Complexity: O(logn)
def majorityElement(self, nums):
    if len(nums) == 1: return nums[0]
    left = self.majorityElement(nums[:len(nums)//2])
    right = self.majorityElement(nums[len(nums)//2:])
    if left == right: # if two side agree on the majority
        return left
    else:             # otherwise, count one of the elements to decide
        return [left, right][nums.count(right) > len(nums)//2]
