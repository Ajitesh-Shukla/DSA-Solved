class Solution:
    def trap(self, height) -> int:
        i, j=0, 0
        while i<len(height)-1:
            if i!=0:
                break
            i+=1
        j=i+1
        tot_wat=0
        while j<len(height):
            