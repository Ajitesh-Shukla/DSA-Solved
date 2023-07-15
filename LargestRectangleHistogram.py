class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[(-1, -1)]
        max_area=0
        j=0
        for j in range(len(heights)):
            if stack:
                while stack and stack[-1][0]>heights[j]:
                    # Area will be the (j-last elem in stack's index+1)*cur_elem's height
                    cur_h=stack.pop(-1)
                    prev_h=stack[-1]
                    max_area=max(max_area, (j-prev_h[1]-1)*cur_h[0])
                stack.append((heights[j], j))
        if stack:
            for i, elem in enumerate(stack):
                if i==0:
                    max_area=max((len(heights))*elem[0], max_area)
                else:
                    max_area=max((len(heights)-stack[i-1][1]-1)*elem[0], max_area)
        return max_area