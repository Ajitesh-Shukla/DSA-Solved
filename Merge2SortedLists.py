# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''Modifying thr pointer changes the original iff you access the next element, that is the same object'''
class Solution:
    def mergeTwoLists(self, list1, list2):
        '''Take two pointers, one in list1 and another in list2 and iterate'''
        p1=list1  # Modify list1 inplace
        p2=list2
        while p1 and p2:
            if p1.next.val<p2.next.val:
                p1=p1.next
            else:
                temp=p2.next
                p2.next=p1
                p1=p2
                p2=temp
        
        return list1