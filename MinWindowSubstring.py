class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''Neetcode approach
        Take a sliding window, insteading of comparing everything everytime, take a count of haves and needs
        Whenever an element from target is observed inrement its score in source map, if it exactly matches the target
        map, that means, it is equal to it for the first time, increment have by 1
        when have==need, start removing elements from the left till again have != need'''

        tar={c:0 for c in t}
        src={c:0 for c in s}   # Store everything in the window
        for elem in t:
            tar[elem]+=1

        have, need=0, len(tar.keys())   # These save us the need to check each and every value in map all the time
        l=0
        min_res, min_len= None, None
        for r in range(len(s)):
            src[s[r]]+=1
            if s[r] in tar and src[s[r]]==tar[s[r]]:
                have+=1
            if have==need:
                while have==need:
                    src[s[l]]-=1
                    if s[l] in tar and src[s[l]]<tar[s[l]]:
                        have-=1
                    if not min_len or r-l+1<min_len:
                        min_len=r-l+1
                        min_res=s[l:r+1]
                    l+=1
        if not min_res:
            return ""
        return min_res


                
        

                
