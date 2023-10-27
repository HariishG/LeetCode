class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            for _ in range(2):
                j=i
                k=i+_
                while j>=0 and k<len(s):
                    if s[j:k+1]==s[j:k+1][::-1] and len(s[j:k+1])>len(ans):
                        ans=s[j:k+1]
                        j-=1
                        k+=1
                    elif s[j:k+1]==s[j:k+1][::-1]:
                        j-=1
                        k+=1
                    else:
                        break
        return ans
