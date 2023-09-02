class Solution:
    def combinationSum_2(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        cur=[]
        candidates.sort()
        def comb(i, cur_sum_):

            if cur_sum_==target:
                res.append(cur.copy())
                return

            if i>=len(candidates) or cur_sum_>target:
                return
            
            # Either take the elem, with all elements ahead of it with the same value, or skip
            comb(i+1, cur_sum_)

            present_elem=candidates[i]
            sum_=0
            step=i
            print(cur)
            while i<len(candidates) and candidates[i]==present_elem:
                sum_+=candidates[i]
                cur.append(candidates[i])
                i+=1
            comb(i, cur_sum_+sum_)
            while i>step:
                cur.pop()
                i-=1
            return
        
        comb(0, 0)
        return res