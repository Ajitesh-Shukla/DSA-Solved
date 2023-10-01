class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        '''Non MLE sol, essentially we have to add everytime we receive a start
        and subtract everytime we see an end, thus no need to store values
        just iterate'''
        all_times=[(a[0], 1)  for a in A]    # 0 for start, 1 for end: No, use 1 for start, since we need it subtracted before being added due to the corner case
        all_times2=[(a[1], 0)  for a in A]
        all=all_times+all_times2
        all.sort()   # Sort is needed
        max_sum=0
        cur_sum=0
        for elem in all:
            if elem[1]==1:
                cur_sum+=1
            else:
                cur_sum-=1
            max_sum=max(max_sum, cur_sum)
        return max_sum

        


        # '''Just neet max no of meetings taking place at any particular time
        # Find what's the name of this algorithm
        # Always check what is considered as overlapping, here ending and another starting from same is 
        # not considered overlap
        # MLE with this'''
        # # create an array from min to max
        # start=[a[0] for a in A]
        # end=[a[1] for a in A]
        # i, j=min(start), max(end)

        # all_time=[0 for k in range(i, j+1)]

        # for elem in A:
        #     all_time[elem[0]-i]+=1
        #     all_time[elem[1]-i]-=1
        
        # # Prefix sum approach to get the max no. of rooms
        # pre_sum=[]
        # cur_sum=0
        # for elem in all_time:
        #     cur_sum+=elem
        #     pre_sum.append(cur_sum)

        # return max(pre_sum)