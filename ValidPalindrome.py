import re
class Solution:
    def isPalindrome(self, s) -> bool:
        '''Too simple'''
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i, j=0, len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
