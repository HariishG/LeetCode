class Solution:
    def partitionString(self, s: str) -> int:
        c=0
        t=""
        for i in s:
            if i in t:
                c+=1
                t=i
            else:
                t+=i
        return c+1