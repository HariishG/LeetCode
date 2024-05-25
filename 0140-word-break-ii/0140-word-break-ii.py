class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n=len(s)
        def func(i, sentence, word):
            if i==n:
                if word in wordDict:
                    return [(sentence+" "+word)[1:]]
                return []
            if word in wordDict:
                return func(i+1, sentence+" "+word, s[i])+func(i+1, sentence, word+s[i])
            return func(i+1, sentence, word+s[i])
        return func(0,"","")