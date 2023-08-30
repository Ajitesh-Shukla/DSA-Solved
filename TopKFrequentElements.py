class Solution:
    def topKFrequent(self, nums, k: int):
        '''Map to dictionary->Sort O(nlogn), need better than O(nlogn)
        Important: Dictionary preserves order only after python 3.6
        Try O(n): Reverse the count and element in dictionary and then start from the end
        '''
        # O(n)
        dict_all={}
        for elem in nums:
            if elem in dict_all.keys():
                dict_all[elem]+=1
            else:
                dict_all[elem]=1
        nums_for_count=[[] for i in range(len(nums))]   # Will store elements with given number of occurances (1-N, if any)    
        '''Add the specific numbers at the position of their counts, and read from last'''
        for key, v in dict_all.items():
            nums_for_count[v].append(key)

        # Get the k max occuring ones
        j=0
        ans=[]
        for i in range(len(nums)-1, -1, -1):
            j+=len(nums_for_count[i])
            ans+=nums_for_count[i]
            if j==k:
                return ans