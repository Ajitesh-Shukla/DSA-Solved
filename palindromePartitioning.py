class Solution:
    '''Use indices instead of whole s[start:end+1] to save space'''
    def isPalindrome(self, i, j) -> bool: # To check palindrome
        while i<=j:
            if self.word[i]!=self.word[j]:
                return False
            i+=1
            j-=1
        return True
    
    def partition(self, s: str) -> list[list[str]]:
        def get_pal(start, end):
            self.word=s
            '''Get all possible palindromes of this s[start:end+1]'''

            if len(s[start:end+1])<=1:
                return [[s[start:end+1]]]   # Just 1 possible

            local_pal=[]
            for i in range(end+1-start):
                '''Let's take the s[start:end+1] upto i, and send other for partitioning further'''
                if self.isPalindrome(start, start+i):
                    res_ahead=get_pal(start+i+1, end)
                    for elem in res_ahead:
                        local_pal.append([s[start:end+1][:i+1]]+elem)
            return local_pal
        return get_pal(0, len(s)-1)
