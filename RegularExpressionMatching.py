class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''Brute Force solution, don't act on star, act 1 step before it'''
        def get_match(i, j):
            if i==len(s) and j==len(p):
               return True
            elif i==len(s) and p[j]=='*':
                return True
            elif i==len(s) or j==len(p):
                return False
            

            
        
        return get_match(0, 0)      

