class Solution:
    def minSwaps(self, s: str) -> int:
        i=0
        j=len(s)-1
        count=0
        res=0
        while i<j:
            if s[i]=='[':
                count+=1
            else:
                if count:
                    count-=1
                else:
                    while j>i and s[j]!='[':
                        j-=1
                    count+=1
                    res+=1
            i+=1
        return res