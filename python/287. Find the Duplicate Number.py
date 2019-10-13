#  Floyd's Tortoise and Hare - Time: O(n), Space: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        # find the intersction point
        fast = nums[0]
        slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        # find the entrance of cycle
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
