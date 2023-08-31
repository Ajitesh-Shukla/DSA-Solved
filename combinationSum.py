class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        cur_res=[]
        def get_match(cur_sum, i):
            if cur_sum==target:
                res.append(cur_res.copy())
                return
            if i>=len(candidates) or cur_sum>target:
                return
            
            # compute
            cur_res.append(candidates[i])           
            get_match(cur_sum+candidates[i], i)     # i can be repeated
            cur_res.pop()
            get_match(cur_sum, i+1)                 # Not including i
        
        get_match(0, 0)
        return res