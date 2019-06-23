class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """ 
        while head and head.val == val:
            head = head.next
        
        cur = head
        while cur:
            while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            cur = cur.next
        
        return head
