class Solution:
    def getLucky(self, s: str, k: int) -> int:
        Sum=''
        for i in s:
            val=ord(i)-96
            Sum+=str(ord(i)-96)
        Sum=int(Sum)
        for i in range(k):
            temp=0
            while Sum>0:
                temp+=Sum%10
                Sum//=10
            Sum=temp
        return Sum

        