class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs)==1:
            return [adjacentPairs[0][0], adjacentPairs[0][1]]
        d=defaultdict(list)
        ans=[]
        for i in adjacentPairs:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        se=[]
        for i in d:
            if len(d[i])==1:
                se.append(i)
        s,e=se[0],se[1]
        ans=[s, d[s][0]]
        s=d[s][0]
        for i in range(len(adjacentPairs)-2):
            if ans[-2]!=d[s][0]:
                ans.append(d[s][0])
                s=d[s][0]
            else:
                ans.append(d[s][1])
                s=d[s][1]
        ans.append(e)
        return ans
                