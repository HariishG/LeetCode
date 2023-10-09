class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[]
        n=len(dist)
        for i in range(n):
            time.append(dist[i]/speed[i])
        time.sort()
        s=0
        for i in range(n):
            if time[i]<=s:
                return i
            s+=1
        return n
                