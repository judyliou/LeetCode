class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        while rowIndex:
            row = [1] + [a+b for a, b in zip(row[:-1], row[1:])] + [1]
            rowIndex -= 1
        return row
