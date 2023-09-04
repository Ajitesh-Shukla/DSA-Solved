class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        '''Neetcode solution, very smart
        Take a note of both max, and min upto now, use 1 for termination when encountering a 0
        start res as max of the array to avoid edge cases'''
        ans=max(nums)

        curmax, curmin=1,1
        for elem in nums:
            temp=curmax
            curmax=max(elem*curmax, elem*curmin, elem)  # elem itself to handle cases where curmax and curmin are equal
            curmin=min(elem*temp, elem*curmin, elem)
            ans=max(ans, curmax, curmin)

        return ans
