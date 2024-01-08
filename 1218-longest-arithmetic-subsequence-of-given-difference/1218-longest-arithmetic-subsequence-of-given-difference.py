class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n=len(arr)
        index=defaultdict(lambda : -1)
        dp=[1 for _ in range(n)]
        index[arr[0]]=0
        for i in range(1,n):
            idx=index[arr[i]-difference]
            index[arr[i]]=i
            if idx==-1:
                continue
            else:
                dp[i]=dp[idx]+1
        return max(dp)
            