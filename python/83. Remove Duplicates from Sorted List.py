# Solution 1
class Solution(object):
    def examine(self, cur, pre):
        while cur.next != None:
            cur = cur.next
            if cur.val != pre.val:
                pre.next = cur
                pre = cur
            else:
                self.examine(cur, pre)
        pre.next = None
                
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
            
        cur, pre = head, head
        self.examine(cur, pre)
        return head

# Solution 2
class Solution(object):                
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next  # skip repeated ones
            cur = cur.next
        return head
        
