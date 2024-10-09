class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count=0
        res=0
        for i in s:
            if i=='(':
                open_count+=1
            else:
                if open_count:
                    open_count-=1
                else:
                    res+=1
        res+=open_count
        return res