class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        reduced=0
        ans=0
        n=len(happiness)
        for i in range(k):
            if happiness[i]-reduced>0:
                ans+=happiness[i]-reduced
                reduced+=1
            else:
                break
        return ans

