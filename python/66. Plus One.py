# Solution 1
def plusOne(self, digits):
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

# Solution 2
def plusOne(self, digits):    
    num = 0
        level = 1
        for i in range(len(digits)-1, -1, -1):
            num += digits[i] * level
            level *= 10
        num += 1
        return [i for i in str(num)]
