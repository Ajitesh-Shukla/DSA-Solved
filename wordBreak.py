class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dict=set(wordDict)
        '''Tabulate, not exactly tabulate, but uses stack/queue, Also add dp to it, do not repeat elements'''
        '''Also look at tabulation solution later'''
        q=[]
        vis=set()

        for j in range(len(s)):
            if s[:j+1] in dict:
                if j+1==len(s):
                    return True
                q.append(j+1)
                vis.add(j+1)

        while q:
            cur_idx=q.pop()
            if cur_idx==len(s):
                return True
            for j in range(cur_idx, len(s)):
                if s[cur_idx:j+1] in dict and (j+1) not in vis:
                    q.append(j+1)
                    vis.add(j+1)

        return False

        # '''Bruteforce will be to just take every word starting one particular, and then iterate
        # Add dp'''

        # dp=[None for i in range(len(s)+1)]
        # dp[-1]=True

        # def check_word(i):
        #     if i==len(s):
        #         return True
            
        #     if dp[i] is not None:
        #         return dp[i]
            
        #     for j in range(i, len(s)):
        #         if s[i:j+1] in dict:
        #             if check_word(j+1):
        #                 dp[i]=True
        #                 return True
        #     dp[i]=False
        #     return False
        # res=check_word(0)
        # return res