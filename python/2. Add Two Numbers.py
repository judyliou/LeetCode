# Solution 1
def addTwoNumbers(self, l1, l2):
    total = 0
    for i in [l1, l2]:
        digit = 1
        num = 0
        while i != None:
            num += i.val * digit
            digit *= 10
            i = i.next
        total += num

    if total == 0:
        return ListNode(0)
    rtn = cur = ListNode(0)
    while total > 0:
        cur.next = ListNode(total % 10)
        total = total // 10
        cur = cur.next
    return rtn.next
        
# Solution 2
def addTwoNumbers(self, l1, l2):
    rtn = cur = ListNode(0)
    flag = 0
    while l1 != None or l2 != None:
        if l1 == None:
            sum = l2.val + flag
            l2 = l2.next
        elif l2 == None:
            sum = l1.val + flag
            l1 = l1.next
        else:
            sum = l1.val + l2.val + flag
            l1, l2 = l1.next, l2.next

        if sum < 10:
            cur.next = ListNode(sum)
            flag = 0
        else:
            cur.next = ListNode(sum - 10)
            flag = 1
        cur = cur.next
    if flag == 1:
        cur.next = ListNode(1)

    return rtn.next
