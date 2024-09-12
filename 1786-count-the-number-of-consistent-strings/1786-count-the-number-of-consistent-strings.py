class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                ans+=1
        return ans