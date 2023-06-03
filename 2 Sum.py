class Solution:
    def twoSum(self, nums, target: int) :
        '''Take two elements and compare: O(N^2): Rejected
        Sort and then use two pointers O(Nlog(N))
        Use dictionary, just check if target-i is in it O(n)'''

        # Use dictionary
        prev_elem={}
        for i, elem in enumerate(nums):
            res=target-elem   # Check if residual is already in the dict
            if res in prev_elem.keys():
                return [prev_elem[res], i]
            prev_elem[elem]=i  # Store index of each element
            
        # # Sort, then two pointer
        # orig_pos, nums2 = zip(*sorted(enumerate(nums), key=lambda i: i[1]))
        # i, j=0, len(nums2)-1
        # while i<j:
        #     sum_cur=nums2[i]+nums2[j]
        #     print(i, j, sum_cur)
        #     if sum_cur>target:
        #         j-=1
        #     elif sum_cur<target:
        #         i+=1
        #     elif sum_cur==target:
        #         return sorted([orig_pos[i], orig_pos[j]])


        
c=Solution()
nums = [3,2,4]
target = 6
ans=c.twoSum(nums, target)
print(ans)