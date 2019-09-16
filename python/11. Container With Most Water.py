class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxi = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] > height[j]:
                water = height[j] * (j - i)
                j -= 1
            else:
                water = height[i] * (j - i)
                i += 1
            if water > maxi:
                maxi = water
        return maxi
