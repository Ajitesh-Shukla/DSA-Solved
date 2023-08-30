class Solution:
    def trap(self, height) -> int:
        '''Any block can store the min of the two maximas on either side of itself
        Used non two pointer approach here, could use two pointer to save on code complexity'''
        prefix_max=[0] # Stores the max elem on left of an element
        suffix_max=[0] # stores the max elem on the right of an element
        i, j=0, 0  # i stores the max_height
        while i<len(height)-1 and j<len(height)-1:
            if height[j]>height[i]:
                i=j
            prefix_max.append(height[i])
            j+=1
        i, j=len(height)-1, len(height)-1
        while i>0 and j>0:
            if height[j]>height[i]:
                i=j
            suffix_max.append(height[i])
            j-=1
        suffix_max=suffix_max[::-1]

        water=0
        for i, h in enumerate(height):
            min_height=min(prefix_max[i], suffix_max[i])
            if min_height>h:
                water+=(min_height-h)
        return water