class Solution:
    def topKFrequent(self, nums, k: int):
        '''Map to dictionary->Sort O(nlogn)
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
        
        # # map to dictionary->Sort
        # dict_all={}
        # for elem in nums:
        #     if elem in dict_all.keys():
        #         dict_all[elem]+=1
        #     else:
        #         dict_all[elem]=1
        # dict_all=dict(sorted(dict_all.items(), key=lambda item: item[1]))
        # return list(dict_all)[::-1][:k]