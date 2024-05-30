class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n):
            temp=0
            for j in range(i,n):
                temp^=arr[j]
                if temp==0:
                    ans+=j-i
        return ans