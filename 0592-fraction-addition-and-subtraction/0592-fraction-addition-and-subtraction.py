class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0]!='-':
            expression='+'+expression

        i=0
        n=len(expression)
        numerator=[]
        denominator=[]
        lcm=1
        while i<n:
            if expression[i]=='-':
                if i+2<n and  expression[i+2]=='0':
                    numerator.append(-1*int(expression[i+1:i+3]))
                    i+=4
                else:
                    numerator.append(-1*int(expression[i+1]))
                    i+=3
            else:
                if i+2<n and  expression[i+2]=='0':
                    numerator.append(int(expression[i+1:i+3]))
                    i+=4
                else:
                    numerator.append(int(expression[i+1]))
                    i+=3
            
            if i+1<n and  expression[i+1]=='0':
                denominator.append(int(expression[i:i+2]))
                lcm=math.lcm(lcm,int(expression[i:i+2]))
                i+=2
            else:
                denominator.append(int(expression[i]))
                lcm=math.lcm(lcm,int(expression[i]))
                i+=1

        for i in range(len(denominator)):
            numerator[i]*=lcm//denominator[i]
        Sum=sum(numerator)
        return str(Sum//math.gcd(Sum, lcm))+'/'+str(lcm//math.gcd(Sum, lcm))
