class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Naive approach: O((n-k)*k)
        # Take note of the two largest elem in window, take care of k=1
        # Won't work, as we will need the second max when we are out of first and we don't have a third
        # keep sorted array and add the next elements using binary search O((n-k)*log(k))
        # Better??
        

            