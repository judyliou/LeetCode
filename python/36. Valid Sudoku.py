class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        matrix = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9): 
                cur = board[i][j]
                
                if cur != '.':
                    if cur not in rows[i]: rows[i].add(cur)
                    else: return False
                    
                    if cur not in cols[j]: cols[j].add(cur)
                    else: return False
                    
                    m = (i // 3) * 3 + j // 3
                    if cur not in matrix[m]: matrix[m].add(cur)
                    else: return False
        return True
