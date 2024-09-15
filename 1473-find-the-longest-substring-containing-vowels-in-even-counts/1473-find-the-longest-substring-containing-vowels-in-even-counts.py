class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic={(0,0,0,0,0):-1}
        temp=[0,0,0,0,0]
        res=0
        for i in range(len(s)):
            if s[i]=='a':
                temp[0]^=1
            elif s[i]=='e':
                temp[1]^=1
            elif s[i]=='i':
                temp[2]^=1
            elif s[i]=='o':
                temp[3]^=1
            elif s[i]=='u':
                temp[4]^=1
            if tuple(temp) in dic:
                res=max(res,i-dic[tuple(temp)])
            else:
                dic[tuple(temp)]=i
        return res
