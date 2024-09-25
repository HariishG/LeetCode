class TrieNode:
    def __init__(self, val):
        self.val=val
        self.children={}
        self.count=0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root=TrieNode("")
        def constructTrie(word):
            start=root
            for c in word:
                if c not in start.children:
                    start.children[c]=TrieNode(c)
                start=start.children[c]
                start.count+=1
                
        for word in words:
            constructTrie(word)
        res=[0 for _ in range(len(words))]
        for i, word in enumerate(words):
            curr=0
            start=root
            for c in word:
                if c in start.children:
                    start=start.children[c]
                    res[i]+=start.count
                else:
                    break
        return res

        
