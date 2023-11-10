class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d=defaultdict(list)
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
        for i in range(len(adjacentPairs)-1):
            if ans[-2]!=d[s][0]:
                ans.append(d[s][0])
                s=d[s][0]
            else:
                ans.append(d[s][1])
                s=d[s][1]
        return ans
                