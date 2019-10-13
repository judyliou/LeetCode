# Hash Table - Time: O(n), Space: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        if nums is None:
            return False
        else:
            num_dict = {}
            for i in nums:
                if num_dict.get(i) is None:
                    num_dict[i] = 1
                else:
                    return True
            return False
            
# Sorted - Time: O(nlogn), Space: O()
class Solution(object):
    def containsDuplicate(self, nums):
        if nums is None:
            return False
        else:
            nums.sort()
            for i in range(len(nums)-1):
                if (nums[i] - nums[i+1]) == 0:
                    return True
            return False
            
