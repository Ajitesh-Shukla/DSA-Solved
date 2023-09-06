class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        '''Neetcode Solution, O(n)'''




        # '''Tabulate'''
        # dp=[[-1 for i in range(len(prices))] for j in range]
        
        
        
        # '''Bruteforce->dp (store buy-sell pair, also tried index, wasn't fast enough, buy-sell pair
        # is also slow)'''

        # dp=[[-1 for i in range(len(prices))] for j in range(len(prices)-1)]

        # def buy_sell(i):   # return max money possible after an index
        #     if i>=len(prices):
        #         return 0

        #     max_price=0
        #     for buy in range(i, len(prices)-1):
        #         for sell in range(buy+1, len(prices)):
        #             if prices[sell]>prices[buy]:
        #                 print(buy, sell)
        #                 if dp[buy][sell]!=-1:
        #                     cur_price=dp[buy][sell]
        #                 else:
        #                     cur_price=(prices[sell]-prices[buy])+buy_sell(sell+2)
        #                     dp[buy][sell]=cur_price
        #                 if cur_price>max_price:
        #                     max_price=cur_price
        #     return max_price
        # res=buy_sell(0)
        # return res
        