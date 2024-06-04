class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        odd=False
        ans=0
        for i in d:
            if d[i]%2==0:
                ans+=d[i]
            else:
                ans+=d[i]-1
                odd=True
        if odd:
            return ans+1
        return ans
                