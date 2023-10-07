class Solution:
    def get_pow_rec(self, x, n):
        if n==0:
            return 1
        
        # computation, iterate
        calc=self.get_pow_rec(x, n//2)
        if n%2==0:
            return calc*calc
        else:
            return calc*calc*x


    def myPow(self, x: float, n: int) -> float:
        '''Remove some repeated calculation to save time, O(logn)'''
        
        if n>0:
            return self.get_pow_rec(x, n)
        else:
            return 1/self.get_pow_rec(x, -n)