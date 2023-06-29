class Solution:
    '''Taking prime numbers doesn't work here
    Take a list with count of all alphabets
    and get counts of alphabets a-z in s1, then using moving window get corresponding list
    in s2 and compare, use the previous list for the next iteration to reduce time complexity'''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst_s1=[0 for i in range(26)]
        for elem in s1:   
            lst_s1[ord(elem)-ord('a')]+=1
        
        if len(s2)<len(s1):
            return False
        
        lst_s2=[0 for i in range(26)]
        for elem_num in range(len(s1)):   
            lst_s2[ord(s2[elem_num])-ord('a')]+=1

        if lst_s2==lst_s1:
            return True

        for start in range(len(s2)-len(s1)):
            end=start+len(s1)
            # print(start, end)
            lst_s2[ord(s2[start])-ord('a')]-=1
            lst_s2[ord(s2[end])-ord('a')]+=1
            if lst_s2==lst_s1:
                return True
        return False


