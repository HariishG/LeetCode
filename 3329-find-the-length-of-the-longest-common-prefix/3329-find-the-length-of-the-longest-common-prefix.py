class TrieNode:
    def __init__(self,val):
        self.val=val
        self.children={}
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root=TrieNode("")
        def constructTrie(num):
            start=root
            for c in num:
                if c in start.children:
                    start=start.children[c]
                else:
                    start.children[c]=TrieNode(c)
                    start=start.children[c]
        for num in arr1:
            constructTrie(str(num))
        ans=0
        for num in arr2:
            curr=0
            start=root
            for c in str(num):
                if c in start.children:
                    start=start.children[c]
                    curr+=1
                else:
                    break
            ans=max(ans,curr)
        return ans
                    