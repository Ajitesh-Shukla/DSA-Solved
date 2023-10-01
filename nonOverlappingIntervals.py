class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        '''Compare pairwise, and remove one of two depending on whichever one
        ends last
        Since at one particular position, we have to keep just one, so pair approach also works
        it is a greedy approach'''

        intervals.sort()
        to_remove=0
        start=intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0]<start[1]:     # Overlapping
                '''Remove the one that is bigger after match point, int[i][0]
                as one must definitely go'''
                if intervals[i][1]<start[1]:
                    start=intervals[i]
                to_remove+=1
            else:
                start=intervals[i]
        return to_remove





        