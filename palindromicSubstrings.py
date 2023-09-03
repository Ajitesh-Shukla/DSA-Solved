class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        '''O(n^2 solution, check from every element taking it as the mid of a palindromic string)'''
        '''What is dp about it???'''
        for alpha in range(len(s)):
            # Check odd length
            i, j=alpha, alpha
            while i>=0 and j<len(s) and s[i]==s[j]:
                ans+=1
                i-=1
                j+=1
            # check even length
            i, j=alpha, alpha+1  # No need to do -1, will be taken care in this approach from one of those two
            while i>=0 and j<len(s) and s[i]==s[j]:
                ans+=1
                i-=1
                j+=1

        return ans    
