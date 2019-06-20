class Solution:
    # @param n, an integer
    # @return an integer
    
    # Solution 1
    def reverseBits(self, n):
        input = '{:032b}'.format(n)
        reverse = input[::-1]
        output = int(reverse, 2)
        return output
