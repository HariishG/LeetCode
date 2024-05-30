class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        pre=[0]
        for i in range(n):
            pre.append(pre[-1]^arr[i])
        
        for i in range(n+1):
            for j in range(i+1, n+1):
                if pre[i]==pre[j]:
                    ans+=j-i-1
        return ans