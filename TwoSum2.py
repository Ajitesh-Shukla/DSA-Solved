class Solution:
    def twoSum(self, numbers, target: int) :
        '''Array is sorted, use two pointers'''
        i, j=0, len(numbers)-1
        while i<=j:
            sum_cur=numbers[i]+numbers[j]
            if sum_cur==target:
                return [i+1, j+1]
            elif sum_cur<target: # Need to increment the smaller one
                i+=1
            else:
                j-=1
                