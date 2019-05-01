# Solution 1
class Solution(object):
    def addBinary(self, a, b):
        a = int(a)
        b = int(b)
        total = [int(x) for x in str(a + b)]
        for i in range(len(total)-1, 0, -1):
            if total[i] >= 2:
                total[i-1] += 1
                total[i] = total[i] - 2

        if total[0] >= 2:
            total[0] = total[0] - 2
            total.insert(0, 1)
            
        return "".join([str(i) for i in total])


# Solution 2
class Solution(object):
    def addBinary(self, a, b):
        total = int(a, 2) + int(b, 2)
        return bin(total)[2:]
