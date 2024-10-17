class Solution:
    def maximumSwap(self, num: int) -> int:
        num=str(num)
        n=len(num)
        idx=[None for _ in range(10)]
        for i in range(n-1,-1,-1):
            if not(idx[int(num[i])]):
                idx[int(num[i])]=i
        s=0
        print(idx)
        while s<n:
            bit=int(num[s])
            for i in range(9,bit,-1):
                if idx[i] and idx[i]>s:
                    print(s,idx[i])
                    return int(num[:s]+num[idx[i]]+num[s+1:idx[i]]+num[s]+num[idx[i]+1:])
            s+=1
        return int(''.join(num))