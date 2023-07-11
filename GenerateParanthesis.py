def next_elem(cur_str, open, close, n):
    # Base
    if open==n and close==n:
        return ['']
    elif open==n and close<n:
        return [')'+elem for elem in next_elem(cur_str, open, close+1, n)]
    
    # Compute
    arr = ['('+elem for elem in next_elem(cur_str, open+1, close, n)]
    if open>close:
        arr+=[')'+elem for elem in next_elem(cur_str, open, close+1, n)]
    return arr

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        '''At any point, we will have two choices, open or close;
        n>=open>=close'''
        open, close=0, 0
        return next_elem("", open, close, n)
