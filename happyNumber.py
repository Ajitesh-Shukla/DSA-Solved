class Solution:
    def getSquare(self, a):
        '''square the digits and return the sum'''
        n=len(str(a))
        i=0
        sq_sum=0
        while i<n:
            sq_sum+=(a%10)**2
            a=a//10
            i+=1
        return sq_sum

    def isHappy(self, n: int) -> bool:
        track=set()  # Keep track of cycle, either reaches 1 in an inf cycle or another numbered cycle
        while n not in track:
            track.add(n)
            n=self.getSquare(n)
        if n==1:
            return True
        return False
            


