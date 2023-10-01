class Solution:
    def merge(self, intervals):
        '''Roughly the same approach as insertInterval, keep expanding merged interval till you can'''
        intervals.sort()
        res=[]
        inter=[]
        for i in range(len(intervals)):
            if not inter:
                inter=intervals[i]
            elif inter[1]<intervals[i][0]:
                res.append(inter)
                inter=intervals[i]
            else:
                inter[1]=max(intervals[i][1], inter[1])
        res.append(inter)
        return res