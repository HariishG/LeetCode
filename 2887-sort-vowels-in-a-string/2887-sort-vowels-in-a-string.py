class Solution:
    def sortVowels(self, s: str) -> str:
        vow=['A','E','I','O','U','a','e','i','o','u']
        dic={'A':0, 'E':0, 'I':0, 'O': 0 ,'U':0,'a':0,'e':0,'i':0,'o':0,'u':0}
        for i in s:
            if i in vow:
                dic[i]+=1
        lst=[]
        for i in vow:
            lst.append([i, dic[i]])
        i=0
        n=10
        while i<n:
            if lst[i][1]==0:
                lst.pop(i)
                n-=1
            else:
                i+=1
        for i in range(len(s)):
            if s[i] in vow:
                s=s[:i]+lst[0][0]+s[i+1:]
                lst[0][1]-=1
                if lst[0][1]==0:
                    lst.pop(0)
        return s

              


        # vow=['A','E','I','O','U','a','e','i','o','u']
        # for i in range(len(s)):
        #     start=-1
        #     j=0
        #     while j<len(s):
        #         if s[j] not in vow:
        #             j+=1
        #             continue
        #         else:
        #             pos=j
        #             j+=1
        #             while j<len(s) and s[j] not in vow:
        #                 j+=1
        #                 continue
        #             if j<len(s) and ord(s[pos])>ord(s[j]):
        #                 s=s[:pos]+s[j]+s[pos+1:j]+s[pos]+s[j+1:]
        # return s
