class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        ind1=0
        ind2=0
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                continue
            ind1=i
            i+=1
            break
        else:
            return True
        for j in range(i,len(s1)):
            if s1[j]==s2[j]:
                continue
            ind2=j
            break
        if s1[ind1]==s2[ind2] and s1[ind2]==s2[ind1] and s1[ind2+1:]==s2[ind2+1:]:
            return True
        return False

        
        
        