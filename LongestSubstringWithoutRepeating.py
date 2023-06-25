# def get_idx(lst, elem):
#     for i, elem2 in enumerate(lst):
#         if elem2==elem:
#             return i
#     return -1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Get better, O(n) solution:
        Store index in the sliding window as well
        update whenever repeat elem is encountered and initialize the start index for window'''
        all_elem={}
        max_len=0
        start_idx=0
        for idx, elem in enumerate(s):
            if elem not in all_elem.keys():
                all_elem[elem]=idx
            else:
                max_len=max(max_len, idx-start_idx)
                start_idx=max(start_idx, all_elem[elem]+1)
                all_elem[elem]=idx
            # print(all_elem, start_idx)
        return max(max_len, len(s)-start_idx)   # For the current elements in dictionary
                
        # '''O(n): use a set to store elements untill now, 
        # if repeated get max len and reinitialize set
        # Won't work, as we need not necessarily reinitialize set, 
        # can just remove first element sometimes, that will be a list and hence O(nsq)'''
        # cur_elem=[]
        # max_len=0
        # for elem in s:
        #     if elem in cur_elem:
        #         max_len=max(max_len, len(cur_elem))
        #         cur_elem=cur_elem[get_idx(cur_elem, elem)+1:]
        #     cur_elem.append(elem)
        # return max(max_len, len(cur_elem))
    