def check_critical(a, b, first, last):   # a is substring, b is the string to check
    if first not in b.keys():
        return 1
    if last not in b.keys():
        return 0
    if a[first]==b[first] and a[last]==b[last]:
        return -1   # both critical
    elif a[first]==b[first] and a[last]!=b[last]:
        return 0   # First critical
    else:
        return 1   # No critical or last critical

class Solution:
    def minWindow(self, s: str, t: str) -> str:


        # Doesn't work, can't differentiate between two different substrings
        # if len(t)>len(s):
        #     return ""
        # i, j=0, len(s)-1
        # all_elem='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # dict_substr={}
        # dict_t={}
        # for elem in s:
        #     dict_substr[elem]=dict_substr.get(elem, 0)+1
        # for elem in t:
        #     dict_t[elem]=dict_t.get(elem, 0)+1

        # # check if every elem in t is in the full string s
        # for elem in dict_t.keys():
        #     if elem not in dict_substr.keys() or dict_substr[elem]<dict_t[elem]:
        #         return ""

        # '''At every step check if the strings are critical, 
        # i.e. if the elem in t have counts lesser than in s'''
        
        # while i<=j:
        #     idx=check_critical(dict_substr, dict_t, s[i], s[j])
            
        #     if idx==-1:
        #         return s[i:j+1]
        #     elif idx==0:
        #         dict_substr[s[j]]-=1
        #         j-=1

        #     else:
        #         dict_substr[s[i]]-=1
        #         i+=1
        # return s
        
            
        
        