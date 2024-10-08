class Solution:
    def minSwaps(self, s: str) -> int:
        s=list(s)
        n=len(s)
        i=0
        j=n-1
        stack=[]
        res=0
        while i<j:
            if s[i]=='[':
                stack.append(True)
            else:
                if stack:
                    stack.pop()
                else:
                    while j>i and s[j]!='[':
                        j-=1
                    s[j]=']'
                    stack.append(True)
                    res+=1
            i+=1
        return res