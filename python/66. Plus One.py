class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n):
                last = digits.pop()
                if last == 9:
                    continue
                else:
                    digits.append(last + 1)
                    digits.extend([0] * i)
                    return digits
        digits = [1]
        digits.extend([0] * n)
        return digits
