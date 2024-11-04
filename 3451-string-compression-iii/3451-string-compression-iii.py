class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        c=""
        count=0
        for i in word:
            if i==c:
                count+=1
            else:
                if count:
                    comp+=str(count)+c
                c=i
                count=1

            if count==9:
                comp+=str(count)+c
                c=""
                count=0
        if count:
            comp+=str(count)+c
        return comp
