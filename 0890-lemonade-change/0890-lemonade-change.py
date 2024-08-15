class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5=0
        change_10=0
        for i in bills:
            if i==5:
                change_5+=1
            elif i==10:
                if change_5:
                    change_10+=1
                    change_5-=1
                else:
                    return False
            else:
                if change_10 and change_5:
                    change_10-=1
                    change_5-=1
                elif change_5>=3:
                    change_5-=3
                else:
                    return False
        return True

                