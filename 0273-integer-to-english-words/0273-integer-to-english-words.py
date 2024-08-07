class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        def func(n):
            ans=[]
            hundreds=n//100
            if hundreds:
                ans.append(ones[hundreds]+" Hundred")
            onestens=n%100
            if onestens>=20:
                o=onestens%10
                t=onestens//10
                ans.append(tens[t*10])
                if o:
                    ans.append(ones[o])
            
            elif onestens:
                ans.append(ones[onestens])
            return ' '.join(ans)



        postfix=["", " Thousand", " Million", " Billion"]
        i=0
        ans=[]
        while num:
            digits=num%1000
            s=func(digits)
            if s:
                ans=[s+postfix[i]]+ans
            num//=1000
            i+=1
        return  ' '.join(ans)
