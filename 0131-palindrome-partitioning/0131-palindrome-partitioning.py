class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        def func(sub, i):
            if i==n:
                if sub[-1]==sub[-1][::-1]:
                    return [sub]
                return []
            if sub:
                if sub[-1]==sub[-1][::-1]:
                    return func(sub+[s[i]], i+1) + func(sub[:-1]+[sub[-1]+s[i]], i+1)
                return func(sub[:-1]+[sub[-1]+s[i]], i+1)
            return func(sub+[s[i]], i+1)
        return func([], 0)