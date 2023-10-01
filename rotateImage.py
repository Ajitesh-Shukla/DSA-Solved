class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''This ques is just about familiarity with language, tiring and implementation based
        Start from the mid, and increase levels, at each level
        do 4 rotations for each element in row'''
        '''Try to change the different approach followed for odd and even sizes to a single one'''

        n=len(matrix)
        r=n%2
        for level in range(n//2):           # Move out of center
            for i in range(2*level+1+r):      # iterate through all elements of one corner
                start=matrix[n//2-1-level][n//2-1-level+i]
                matrix[n//2-1-level][n//2-1-level+i]=matrix[n//2+r+level-i][n//2-1-level]
                matrix[n//2+r+level-i][n//2-1-level]=matrix[n//2+r+level][n//2+r+level-i]
                matrix[n//2+r+level][n//2+r+level-i]=matrix[n//2-1-level+i][n//2+r+level]
                matrix[n//2-1-level+i][n//2+r+level]=start



