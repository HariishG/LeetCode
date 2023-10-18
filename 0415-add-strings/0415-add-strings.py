class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len=max(len(num1), len(num2))
        num1=num1.zfill(max_len)
        num2=num2.zfill(max_len)
        ans=""
        carry=0
        i=max_len-1
        while i>=0:
            d1=int(num1[i])
            d2=int(num2[i])
            ans+=str((d1+d2+carry)%10)
            carry=(d1+d2+carry)//10
            i-=1
        if carry!=0:
            return str(carry)[::-1]+ans[::-1]
        return ans[::-1]
