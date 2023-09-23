class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dic={}
        max_chain=0
        for word in words:
            dic[word]=1
            for i in range(len(word)):
                prev_word = word[:i]+word[i+1:]
                if prev_word in dic:
                    dic[word]=max(dic[word], dic[prev_word]+1)
            max_chain=max(max_chain, dic[word])
        return max_chain