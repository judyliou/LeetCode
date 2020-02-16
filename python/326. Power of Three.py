def isPowerOfThree(self, n):
    while n > 1:
        if n % 3 == 0:
            n = int(n / 3)
        else:
            return False
    if n == 1:
        return True
    else:
        return False
