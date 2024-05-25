class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp={}
        def func(i, word):
            if i==n:
                return word in wordDict
            if (i,word) in dp:
                return dp[(i,word)]
            dp[(i,word)]=False
            if word in wordDict:
                dp[(i,word)] |= func(i+1, s[i])
            dp[(i,word)] |= func(i+1, word+s[i])
            return dp[(i,word)]
        return func(0,"")