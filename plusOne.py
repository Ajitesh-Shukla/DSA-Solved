class Solution:
    def plusOne(self, digits):
        '''Simple straightforward approach'''
        n=len(digits)
        carry=1
        for i in range(n-1, -1, -1):
            cur_sum=(carry+digits[i])%10
            carry=(carry+digits[i])//10
            digits[i]=cur_sum
        if carry!=0:
            return [carry]+digits
        return digits
