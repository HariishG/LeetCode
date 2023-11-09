class Solution:
    def countHomogenous(self, s: str) -> int:
        subs=[]
        curr=s[0]
        for i in range(1, len(s)):
            if s[i]==curr[-1]:
                curr+=s[i]
            else:
                subs.append(curr)
                curr=s[i]
        subs.append(curr)
        ans=0
        for i in subs:
            ans+=(len(i)*(len(i)+1))//2
        return ans % (10**9+7)
            