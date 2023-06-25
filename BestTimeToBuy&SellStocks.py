class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''Simple method: O(nsq), check max profit for every element'''
        '''Moving window, keep track of min untill now and a max profit, 
        obtained from selling just now'''
        min_now=prices[0]
        max_profit=0
        j=1
        while j<len(prices):
            if prices[j]<min_now:
                min_now=prices[j]
            else:
                max_profit=max(max_profit, prices[j]-min_now)
        return max_profit