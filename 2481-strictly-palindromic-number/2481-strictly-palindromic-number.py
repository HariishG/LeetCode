class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return str(bin(n))[2:]==str(bin(n))[::1]