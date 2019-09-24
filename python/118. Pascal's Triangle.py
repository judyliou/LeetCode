# Solution 1
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        res = [[1]]
        if numRows == 1: return res
        
        for i in range(1, numRows):
            line = [1]
            for j in range(i-1):
                line.append(res[i-1][j] + res[i-1][j+1])
            line.append(1)
            res.append(line)
        return res


# Solution 2
class Solution(object):
    def generate(self, numRows):
        if numRows == 0: return []
        ret = [[1]]
        numRows -= 1
        while numRows > 0:
            ret.append([1] + [a+b for a, b in zip(ret[-1][:-1], ret[-1][1:])] + [1])
            numRows -= 1
        return ret
    
