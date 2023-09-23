class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        '''Brute force, calculate the max sequence for each element O(n^4)->Memoization'''
        m, n = len(matrix), len(matrix[0]) # mxn matrix
        score=[[-1 for i in range(n)] for j in range(m)]

        dx=[[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, vis):   # Make it to return length
            if score[i][j]!=-1:
                return score[i][j]
            l=[1,1,1,1]
            for k, elem in enumerate(dx):
                di, dj=i+elem[0], j+elem[1]
                if di<m and dj<n and di>=0 and dj>=0 and (di, dj) not in vis and matrix[di][dj]>matrix[i][j]:
                    vis.add((di, dj))
                    l[k]+=dfs(di, dj, vis)
                    vis.remove((di, dj))
            score[i][j]=max(l)
            return score[i][j]
                
        max_score=1
        for i in range(m):
            for j in range(n):
                '''Do bfs for every element, bfs won't work in it's simple formsince we need length as well'''
                max_score=max(max_score, dfs(i, j, set()))

        return max_score
        



        