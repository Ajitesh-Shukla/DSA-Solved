from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''Only alphabets (26) so can get longest chain w.r.t each one and then get the max
        Problem reduces to getting max chain for one single alphabel given k
        Storing k elements so O(N), still slow as it is O(26N)'''
        # Try for getting longest chain for A, then continue
        '''See Neetcode's solution as well'''
        all_alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        max_all=0
        for alpha in all_alpha:
            start, other_elems, end, k_elem=0, deque([]), 0, k
            max_len=0
            while end<len(s):
                if s[end]!=alpha:
                    if k_elem==0:
                        max_len=max(max_len, end-start)
                        try:
                            start=other_elems.popleft()+1
                        except:
                            start=end+1
                    else:
                        k_elem-=1
                    other_elems.append(end)
                end+=1
            # print(alpha, max(max_len, len(s)-start))
            max_all=max(max_all, max(max_len, len(s)-start))
        return max_all