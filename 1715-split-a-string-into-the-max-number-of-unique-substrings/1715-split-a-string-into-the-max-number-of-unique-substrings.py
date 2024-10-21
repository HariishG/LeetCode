class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def func(i, sub, p):
            if i==len(s):
                if found[sub]:
                    return 0
                return p+1
            take=0
            if not(found[sub]):
                found[sub]=True
                take=func(i+1, s[i], p+1)
                found[sub]=False
            not_take=func(i+1, sub+s[i], p)
            return max(take, not_take)
        found=defaultdict(bool)
        found[""]=True
        return func(0,"", 0)
            