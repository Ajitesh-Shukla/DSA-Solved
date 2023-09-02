class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        '''straightforward
        For saving on memory, reuse the cost array
        use tabulation instead of memoization (no recursive implementation, efficient memory)'''

        for i in range(len(cost)-3, -1, -1):
            cost[i]+=min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])