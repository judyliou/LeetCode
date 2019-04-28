# Solution 1 (recursive)
class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
     
        pre = self.countAndSay(n-1)
        read = ""
        count = 0
        curr = pre[0]
        for i in pre:
            if curr == i:
                count += 1
            else:
                read += str(count) + curr
                curr = i
                count = 1
        read += str(count) + curr
        return read


# Solution 2 (iterative)
class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
     
        pre = '1'
        for i in range(1, n):
            read = ""
            count = 0
            p = pre[0]
            for j in range(len(pre)):
                c = pre[j]
                if p == c:
                    count += 1
                else:
                    read += str(count) + p
                    p = c
                    count = 1
            read += str(count) + p
            pre = read
        return pre
