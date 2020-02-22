class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        prev = head_prev = ListNode(0)
        prev.next = cur = head
        while cur:
            flag = 0
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
                flag = 1
            if flag == 1:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head_prev.next
