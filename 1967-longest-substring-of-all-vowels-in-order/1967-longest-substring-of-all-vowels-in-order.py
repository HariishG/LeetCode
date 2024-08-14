class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans=0
        i=0
        n=len(word)
        while i<n:
            curr=1
            d={'a':False, 'e':False, 'i':False, 'o':False, 'u':False}
            d[word[i]]=True
            while i+1<n and ord(word[i])<=ord(word[i+1]):
                curr+=1
                d[word[i+1]]=True
                i+=1
            print(d['u']==True)
            if d['a']==True and d['e']==True and d['i']==True and d['o']==True and d['u']==True:
                ans=max(ans, curr)
            i+=1
        return ans
