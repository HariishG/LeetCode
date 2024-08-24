class Solution:
    def nearestPalindromic(self, n: str) -> str:
        cases=[]
        ln=len(n)
        if ln%2==1:
            cases.append(int(n[:ln//2+1]+n[:ln//2][::-1]))
            cases.append(int(str(int(n[:ln//2+1])-1)+str(int(n[:ln//2+1])-1)[:-1][::-1]))
            cases.append(int(str(int(n[:ln//2+1])+1)+str(int(n[:ln//2+1])+1)[:-1][::-1]))
        else:
            cases.append(int(n[:ln//2]+n[:ln//2][::-1]))
            cases.append(int(str(int(n[:ln//2])-1)+str(int(n[:ln//2])-1)[::-1]))
            cases.append(int(str(int(n[:ln//2])+1)+str(int(n[:ln//2])+1)[::-1]))
        cases.append(10**ln+1)
        cases.append(10**(ln-1)-1)
        ans=float('inf')
        print(cases)
        cases.sort()
        for i in cases:
            if i!=int(n) and abs(i-int(n))<abs(ans-int(n)):
                ans=i
        return str(ans)