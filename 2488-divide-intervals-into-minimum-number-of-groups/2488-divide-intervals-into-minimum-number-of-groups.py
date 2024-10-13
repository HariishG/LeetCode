class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start=[]
        end=[]
        for s,e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()

        i=0
        j=0
        res=0
        while i<len(intervals):
            if start[i]<=end[j]:
                i+=1
            else:
                j+=1
            res=max(res, i-j)
        return res