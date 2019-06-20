class Solution:
    # @param n, an integer
    # @return an integer
    
    # Solution 1
    def reverseBits(self, n):
        input = '{:032b}'.format(n)
        reverse = input[::-1]
        output = int(reverse, 2)
        return output
    
    # Solution 2
    def reverseBits(self, n):
        reverse = 0
        for i in range(32):
            reverse = reverse << 1
            reverse |= (n >> i) & 1
        return reverse
