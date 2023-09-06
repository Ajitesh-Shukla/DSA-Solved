a = "AGGTAB"
b = "GXTXAYB"    
len_min=min(len(a), len(b))

def lcs_dp(a, b):
    dp=[[0 for i in range(len(a)+1)] for j in range(len(b)+1)]  # bxa
    '''Tabulation'''
    dp2=[0 for i in range(len(a)+1)] # Perform the same operation using a 1D array

    for i in range(len(b)-1, -1, -1):
        dp3=[0 for i in range(len(a)+1)]   # Array for next iteration
        for j in range(len(a)-1, -1, -1):
            if b[i]==a[j]:
                dp3[j]=1+dp2[j+1]
            else:
                dp3[j]=max(dp2[j], dp3[j+1])
        dp2=dp3.copy()

    return dp2[0]
    
    # '''Memoization'''
    # dp=[[-1 for i in range(len(a))] for j in range(len(b))]  # bxa
    # def dp_(i, j):
    #     if i==len(b) or j==len(a):
    #         return 0  
        
    #     if dp[i][j]!=-1:
    #         return dp[i][j]
        
    #     if a[j]==b[i]:
    #         dp[i][j]=1+dp_(i+1, j+1)
    #     else:
    #         dp[i][j]=max(dp_(i+1, j), dp_(i, j+1))
    #     return dp[i][j]
    
    # res=dp_(0, 0)
    # print(dp)
    # return res

print(lcs_dp("abcde", "ace"))

# def lcs(idx_a, idx_b):
#     if idx_a==len(a) or idx_b==len(b):
#         return 0
#     if a[idx_a]==b[idx_b]:
#         return 1+lcs(idx_a+1, idx_b+1)
#     else:
#         return max(lcs(idx_a+1, idx_b), lcs(idx_a, idx_b+1))

# print(lcs(0, 0))