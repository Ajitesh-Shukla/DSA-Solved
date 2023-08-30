class Solution:
    def longestConsecutive(self, nums) -> int:
        '''No sorting, since O(n) 'time' is req
        Look for hashing: See solution
        '''
        # Every sequence has a start and an end, conert the list to a set and check if the set has numbers
        # to the left and the right of each number
        # This way you determine which numbers start, and which ones end sequences
        '''A set contains all unique elements'''
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence, compute only for the starting points of sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:   # Coninue up until you get endpoint
                    length += 1
                longest = max(length, longest)
        return longest
