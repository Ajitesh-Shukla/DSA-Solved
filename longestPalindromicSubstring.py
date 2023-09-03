class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len=[0]
        max_str=['']
        # using dp, store if (i, j) is a palindrome, O(n^2), LLE, try for O(n), 1D dp
        # Try map
        # DP actually not needed, just take every element and expand both/one side
        dp=[[None for i in range(len(s))] for j in range(len(s))]
        def check(i, j):  # To check if  from i to j is a palindrome
            # Base case
            if i==j or (i==j-1 and s[i]==s[j]):
                if j-i+1>max_len[0]:
                    max_len[0]=j-i+1
                    max_str[0]=s[i:j+1]
                dp[i][j]=True
                return True
            if (i==j-1 and s[i]!=s[j]):
                dp[i][j]=False
                return False  
            if dp[i][j] is not None:
                return dp[i][j]
            
            # computation
            if s[i]!=s[j]:
                dp[i][j]=False
                return dp[i][j]
            res=check(i+1, j-1)  # Check for the inside element
            if res:
                dp[i][j]=True
                if j-i+1>max_len[0]:
                    max_len[0]=j-i+1
                    max_str[0]=s[i:j+1]
                return dp[i][j]

        for i in range(len(s)):
            for j in range(i, len(s)):
                check(i, j)
        return max_str[0]
        

            
            