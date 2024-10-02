class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        arr2=sorted(set(arr))
        rank=1
        for i in arr2:
            d[i]=rank
            rank+=1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr