class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return True

        s1=sentence1.split()
        s2=sentence2.split()
        n1=len(s1)
        n2=len(s2)
        
        while n1 and n2 and s1[-1]==s2[-1]:
            s1.pop()
            s2.pop()
            n1-=1
            n2-=1
        i=0
        while n1 and n2 and s1[i]==s2[i]:
            n1-=1
            n2-=1
            i+=1
            
        return n1==0 or n2==0