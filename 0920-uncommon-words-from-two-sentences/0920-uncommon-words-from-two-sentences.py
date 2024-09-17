class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d=Counter((s1+' '+s2).split(' '))
        return [i for i in d if d[i]==1]