class Solution:    
    def insert(self, intervals, newInterval):
        '''Always confused in this problem, improve thinking, 
        don't create multiple if conditions
        Neetcode solution very simple, no use of multiple ifs
        newInterval keeps expanding as it merges with other intervals
        Takes all cases from my code in a single pass'''
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # newInterval ends before start of this
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # newInterval is out of influence of this one, so add this
                res.append(intervals[i])
            else:   # Overlapping is there, expand newInterval
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)   # newInterval hasn't ended
        return res
    

# class Solution:
#     def overlap(self, a, b):
#         if max(a)>=min(b) and min(a)<=max(b):
#             return True
#         return False
    
#     def insert(self, intervals, newInterval):
        
#         # Overlapping case
#         res=[]
#         i=0
#         while i<len(intervals):
#             if self.overlap(newInterval, intervals[i]):   # First time of overlap
#                 start=min(newInterval[0], intervals[i][0])
#                 while i<len(intervals) and self.overlap(newInterval, intervals[i]):
#                     i+=1
#                 i-=1   # Stores the last element that overlaps with the interval
#                 res.append([start, max(newInterval[1], intervals[i][1])])
#                 res+=intervals[i+1:]
#                 return res
#             else:
#                 res.append(intervals[i])
#             i+=1
        
#         # Non overlapping case
#         return sorted(intervals+[newInterval])

                





        

        


