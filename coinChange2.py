class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        '''More efficient dp, just use one array'''
        dp=[0 for i in range(amount+1)]
        dp[-1]=1
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount, -1, -1):
                val_dp=0
                cur_am=amount-j
                look_right=cur_am-coins[i]
                if look_right>=0:
                    val_dp+=dp[amount-look_right]
                val_dp+=dp[j]
                dp[j]=val_dp
        return dp[0]


        # '''Tabulation'''
        # dp=[[1 for i in range(amount+1)] for j in range(len(coins))]
        # for i in range(amount-1, -1, -1):
        #     for j in range(len(coins)-1, -1, -1):
        #         val_dp=0
        #         cur_am=amount-i
        #         look_right=cur_am-coins[j]
        #         if look_right>=0:
        #             val_dp+=dp[j][amount-look_right]
        #         if j!=len(coins)-1:
        #             val_dp+=dp[j+1][i]
        #         dp[j][i]=val_dp
        # return dp[0][0]


        # '''Recursion -> dp (store i, cur_amount in dp)
        # Only cur amount is not enough since it will give us duplicates, which was not an issue with coin 
        # change 1, but here it matters, since we count possible path
        # dp qill store possible paths starting i, when we arrive with a particular amount'''
        # dp=[[-1 for i in range(amount)] for j in range(len(coins))] # Number of paths starting i, also need to add an amount to it
        
        # def get_num(i, cur_amount):
        #     if cur_amount==amount:
        #         return 1
        #     if i>=len(coins) or cur_amount>amount:
        #         return 0
        #     if dp[i][cur_amount]!=-1:
        #         return dp[i][cur_amount]
            
        #     num=0
        #     for j in range(i, len(coins)):
        #         num+=get_num(j, cur_amount+coins[j])
        #     dp[i][cur_amount]=num
        #     return num
        # res=get_num(0, 0)
        # return res
