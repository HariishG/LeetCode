class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        Min=float('inf')
        Min_index=-1
        Max=float('-inf')
        Max_index=-1
        for i,arr in enumerate(arrays):
            if arr[0]<Min:
                Min=arr[0]
                Min_index=i
            if arr[-1]>Max:
                Max=arr[-1]
                Max_index=i
        if Min_index!=Max_index:
            return abs(Max-Min)
        ans=0
        print(Min_index)
        for i,arr in enumerate(arrays):
            if i!=Min_index:
                ans=max(ans, abs(Max-arr[0]), abs(arr[-1]-Min))
        return ans
        