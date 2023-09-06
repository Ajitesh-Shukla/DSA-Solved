# import sys
# sys.setrecursionlimit(10000)
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # '''Tabulation'''
        # dp=[-1 for i in range(amount+1)]
        # dp[0]=0
        # for i in range(1, len(dp)):
            
        #     min_p=float('inf')
        #     for coin in coins:
        #         if coin<=i:
        #             min_p=min(min_p, 1+dp[i-coin])
        #     dp[i]=min_p
        # if dp[amount]==float('inf'):
        #     return -1
        # return dp[amount]

        '''Use dp to solve in apt time and memory'''
        '''What to store in dp??? Store min coins req. for a particular amount'''

        # dp=[-1 for i in range(amount+1)]
        # dp[0]=0
        # '''A function to return the minimum req from this particular amount'''
        # def get_min(i, cur_amount, vis):
        #     if cur_amount<0:
        #         return float('inf')
        #     if cur_amount==0:
        #         print(len(vis), vis)
        #     if dp[cur_amount]!=-1:
        #         return dp[cur_amount]
            
        #     min_res_cur=float('inf')
        #     '''Why did changing start index from i to 0 made such difference???
        #     Any combiation is possible even starting with i; 
        #     If we reverse the coins matrix, even i works, why???
        #     DP stores cur_amount, not j. We need, min possible for a given cur amount, doesn't matter
        #     what the previous val was. We need fresh new elements. Thus j is req, if no dp, it will work'''
        #     for j in range(0, len(coins)):
        #         vis.append(coins[j])
        #         res_cur=1+get_min(j, cur_amount-coins[j], vis)
        #         min_res_cur=min(min_res_cur, res_cur)
        #         vis.pop()
        #     dp[cur_amount]=min_res_cur
        #     return min_res_cur
        
        # res=get_min(0, amount, [])
        # print(dp)
        
        # if res==float('inf'): return -1
        # return res
    

        '''recursion'''
        '''A function to return the minimum req from this particular amount'''
        def get_min(i, cur_amount, vis):
            if cur_amount<0:
                return float('inf')
            if cur_amount==0:
                return 0
            
            min_res_cur=float('inf')
            '''Why did changing start index from i to 0 made such difference???
            Any combiation is possible even starting with i; 
            If we reverse the coins matrix, even i works, why???
            -> DP stores cur_amount, not j. We need, min possible for a given cur amount, doesn't matter
            what the previous val was. We need fresh new elements. Thus j is req, if no dp,
            with simple recursion, it will work'''
            for j in range(i, len(coins)):
                vis.append(coins[j])
                res_cur=1+get_min(j, cur_amount-coins[j], vis)
                min_res_cur=min(min_res_cur, res_cur)
                vis.pop()
            return min_res_cur
        
        res=get_min(0, amount, [])
        
        if res==float('inf'): return -1
        return res