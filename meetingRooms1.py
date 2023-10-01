class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        '''Determine if a person could attend all meetings'''
        '''Essentially determine if overlap is there'''
        A.sort()
        start=A[0]
        for i in range(1, len(A)):
            if A[i][0]<start[1]:
                return False
            start=A[i]
        return True

