class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        '''Naive approach O(nsq), check for every element
        Use stack, where we add each element along with index, 
        and pop if next is greater, else append'''
        stack=[]
        ans=[0 for i in range(len(temperatures))]
        j=0
        while j<len(temperatures):
            while stack:
                if temperatures[j]>stack[-1][0]:
                    last_elem=stack.pop(-1)
                    ans[last_elem[1]]=j-last_elem[1]
                else:
                    break
            stack.append([temperatures[j], j])
            j+=1
        return ans
