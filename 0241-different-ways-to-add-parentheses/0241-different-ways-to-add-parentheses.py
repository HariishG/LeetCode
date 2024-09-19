class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(n1,n2,op):
            if op=='+':
                return n1+n2
            if op=='-':
                return n1-n2
            return n1*n2
        def func(l,r):
            res=[]
            for i in range(l,r+1):
                if expression[i] in ('+', '-', '*'):
                    nums1=func(l, i-1)
                    nums2=func(i+1,r)
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(calc(n1,n2,expression[i]))
            if not(res):
                res.append(int(expression[l:r+1]))
            return res

        return func(0,len(expression)-1)