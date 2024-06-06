class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        lst=sorted(Counter(hand).items())
        n=len(lst)
        for i in range(n-groupSize+1):
            if lst[i][1]==0:
                continue
            for j in range(1, groupSize):
                if lst[i][0]+j==lst[i+j][0] and lst[i+j][1]>=lst[i][1]:
                    lst[i+j]=(lst[i+j][0], lst[i+j][1]-lst[i][1])
                else:
                    return False
            lst[i]=(lst[i][0],0)
        
        for i in lst:
            if i[1]!=0:
                return False
        return True