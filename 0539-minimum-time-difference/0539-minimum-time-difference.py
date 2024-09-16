class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        res=float('inf')
        for i in range(len(timePoints)):
            t1=int(timePoints[i][:2])*60+int(timePoints[i][3:])
            t2=int(timePoints[i-1][:2])*60+int(timePoints[i-1][3:])
            res=min(res,abs(t2-t1), 1440-abs(t2-t1))
        return res
            