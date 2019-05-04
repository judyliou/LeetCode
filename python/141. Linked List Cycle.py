# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: Time complexity : O(n); Space complexity O(n)
class Solution(object):
    def hasCycle(self, head):
        record = set()
        while head is not None:
            if head in record:           
                return True
            else:
                record.add(head)
                head = head.next
        return False
                
# Solution 2: Time complexity : O(n); Space complexity O(1)
class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
            
            
