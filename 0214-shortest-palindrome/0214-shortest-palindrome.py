class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not(s):
            return ""
        for i in range(len(s)-1,-1,-1):
            if s[:i+1]==s[:i+1][::-1]:
                return s[i+1:][::-1]+s
            