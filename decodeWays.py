class Solution:
    def numDecodings(self, s: str) -> int:

        '''Tabulation solution, tabulation is always memory efficient'''
        ans=[0 for i in range(len(s)+1)] 
        ans[-1]=1
        if int(s[-1])>0:
               ans[-2]=1
        for i in range(len(s)-2, -1, -1):

            if int(s[i])!=0:
                ans[i]+=ans[i+1]

                if int(s[i])<2 or (int(s[i])==2 and int(s[i+1])<7):
                    ans[i]+=ans[i+2]

        return ans[0]

        # '''Memoization'''
        # dp=[-1 for i in range(len(s))]

        # def get_code(i): # Get code for ones starting from i
        #     # Base
        #     if i>=len(s) or (i==len(s)-1 and int(s[i])>0):    # One way of decoding if you have reached the end
        #         return 1
            
        #     if dp[i]!=-1:
        #         return dp[i]
            
        #     # Compute
        #     dp[i]=0
        #     if int(s[i])!=0:
        #         dp[i]+=get_code(i+1)

        #         if int(s[i])<2 or (int(s[i])==2 and int(s[i+1])<7):
        #             dp[i]+=get_code(i+2)
        #     return dp[i]
        
        # return get_code(0)
            
                

