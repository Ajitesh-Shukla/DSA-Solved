class Solution:
    def maxArea(self, height) -> int:
        '''O(n^2) is the obvious one, calculate all areas and get the max'''
        '''think O(n) using two pointers'''
        i, j=0, len(height)-1
        max_area=min(height[i], height[j])*(j-i)
        while i<j:
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
            if min(height[i], height[j])*(j-i)>max_area:
                max_area=min(height[i], height[j])*(j-i)
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
c=Solution()
print(c.maxArea(height))
