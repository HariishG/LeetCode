class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic=defaultdict(int)
        for i in edges:
            dic[i[0]]+=1
            dic[i[1]]+=1
        Keymax = max(dic, key= lambda x: dic[x])
        return Keymax