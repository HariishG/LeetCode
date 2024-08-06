class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
        lst=sorted(c.items(), key = lambda x:x[1], reverse=True)
        ans=0
        i=0
        while i<len(lst) and i<8:
            ans+=lst[i][1]
            i+=1
        while i<len(lst) and i<16:
            ans+=2*lst[i][1]
            i+=1
        while i<len(lst) and i<24:
            ans+=3*lst[i][1]
            i+=1
        while i<len(lst) and i<26:
            ans+=4*lst[i][1]
            i+=1
        return ans