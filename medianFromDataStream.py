import heapq
class MedianFinder:
    '''Array will get median in O(n), so we have to do better
    BS could give O(logn), NO, only for search it is, not for addition, so O(n)
    Use two sets, maxheap and minheap'''

    def __init__(self):
        self.max_h=[]
        self.min_h=[]
        heapq.heapify(self.max_h)
        heapq.heapify(self.min_h)

    def addNum(self, num: int) -> None:
        if len(self.max_h)==0 and len(self.min_h)==0:
            heapq.heappush(self.min_h, num)
            '''If num less than second heap, add it to the first one and make lengths even later
            Maintain atleast that max(minheap)<min(max_heap)'''
        elif num<=self.min_h[0]:
            heapq.heappush(self.max_h, -1*num)
        else:
            heapq.heappush(self.min_h, num)
        '''Change lengths if not ideal'''
        if len(self.max_h)>len(self.min_h)+1:
            while len(self.max_h)>len(self.min_h)+1:
                elem=heapq.heappop(self.max_h)*(-1)
                heapq.heappush(self.min_h, elem)

        elif len(self.min_h)>len(self.max_h)+1:
            while len(self.min_h)>len(self.max_h)+1:
                elem=heapq.heappop(self.min_h)*(-1)
                heapq.heappush(self.max_h, elem)

    def findMedian(self) -> float:
        if len(self.max_h)>len(self.min_h):
            return self.max_h[0]*(-1)
        elif len(self.max_h)<len(self.min_h):
            return self.min_h[0]
        else:
            return (self.max_h[0]*(-1)+self.min_h[0])/2