class Solution:
    def spiralOrder(self, matrix):
        '''There are multiple levels and 4 different directions
        take two lengths which denote the possible length and four directions
        If one of m, n becomes 0, the other one will only get 1 chance to complete'''
        m, n=len(matrix)-1, len(matrix[0])
        dir=0
        i, j=0, 0
        traverse=[]
        while m>-1 and n>-1:   # Do -1 instead of 0 sine we want to push one step further in case m/n becomes 0 while n/m doesn't
            if dir==0:
                dj=0
                for dj in range(n):
                    traverse.append(matrix[i][j+dj])
                j+=dj
                i+=1
                n-=1
            if dir==1:
                di=0
                for di in range(m):
                    traverse.append(matrix[i+di][j])
                i+=di
                j-=1
                m-=1
            if dir==2:
                dj=0
                for dj in range(n):
                    traverse.append(matrix[i][j-dj])
                j-=dj
                i-=1
                n-=1
            if dir==3:
                di=0
                for di in range(m):
                    traverse.append(matrix[i-di][j])
                i-=di
                j+=1
                m-=1

            dir=(dir+1)%4

        return traverse



