
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''Sorting, O(nlogn), hashing lowercase alphabets using prime numbers O(n), 
        using dictionary to count O(n)'''
        dict_num={}
        for num_elem in range(ord('a'), ord('z')+1):
            elem=chr(num_elem)
            dict_num[elem]=0
        for elem in s:
            dict_num[elem]+=1
        for elem in t:
            dict_num[elem]-=1
        for keys in dict_num.keys():
            if dict_num[keys]!=0:
                return False
        return True
    
c=Solution()
s = "anagram"
t = "nagaram"
ans=c.isAnagram(s, t)
print(ans)
