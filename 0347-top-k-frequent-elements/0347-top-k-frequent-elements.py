class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        ans=[]
        for i in range(k):
            key=max(dic, key= lambda x: dic[x])
            ans.append(key)
            dic[key]=-1
        return ans