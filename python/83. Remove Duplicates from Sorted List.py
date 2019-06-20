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
