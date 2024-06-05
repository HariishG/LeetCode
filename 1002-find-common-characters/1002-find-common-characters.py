class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n=len(words)
        d=defaultdict(lambda : 100001)
        for i in words:
            c=Counter(i)
            for i in range(97,123):
                d[chr(i)]=min(d[chr(i)], c[chr(i)])
            
        ans=[]
        for i in d:
            for j in range(d[i]):
                ans.append(i)
        return ans
                