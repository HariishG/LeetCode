class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lst=sentence.split()
        dictionary.sort(key=len)
        n=len(lst)
        for i in range(n):
            for w in dictionary:
                if lst[i][:len(w)]==w:
                    lst[i]=lst[i][:len(w)]
                    break
        return ' '.join(lst)