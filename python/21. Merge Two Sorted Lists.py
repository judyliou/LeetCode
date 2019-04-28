# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val <= l2.val:
            start = l1
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2
            start.next = self.mergeTwoLists(l1, l2.next)
       
        
        return start


# Solution 2
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val <= l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next    
        temp = start
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2
        
        return start
    
