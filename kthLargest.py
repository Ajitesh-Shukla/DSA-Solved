import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums=[elem*(-1) for elem in nums]
        heapq.heapify(nums)
        i=0
        while i<k-1:
            heapq.heappop(nums)
            i+=1
        return nums[0]*(-1)
