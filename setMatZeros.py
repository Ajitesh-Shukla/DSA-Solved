class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''O(m+n) space when we store all rows and colums, constant space
        when we label elements as out of scope elem (not feasible due to signed int), but O(n^3) time'''
        '''Just modify the O(m+n) algo, and use that extra matrix as the 1st row and 1st col
        for overlap, store an extra variable to get the status of 1st row'''

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        '''see first row and col at last'''
        if matrix[0][0] == 0: 
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        

