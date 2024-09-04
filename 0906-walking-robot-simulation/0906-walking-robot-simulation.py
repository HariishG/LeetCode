class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dic=defaultdict(bool)
        for i in obstacles:
            dic[(i[0],i[1])]=True
        s=[0,0]
        d=0
        ans=0
        for i in commands:
            if i==-1:
                d=(d+1)%4
            elif i==-2:
                d=(d-1)%4
            else:
                if d==0:
                    while i>0 and dic[(s[0],s[1]+1)]!=True:
                        s=[s[0],s[1]+1]
                        i-=1
                elif d==1:
                    while i>0 and dic[(s[0]+1,s[1])]!=True:
                        s=[s[0]+1,s[1]]
                        i-=1
                elif d==2:
                    while i>0 and dic[(s[0],s[1]-1)]!=True:
                        s=[s[0],s[1]-1]
                        i-=1
                else:
                    while i>0 and dic[(s[0]-1,s[1])]!=True:
                        s=[s[0]-1,s[1]]
                        i-=1
                ans=max(ans, s[0]**2+s[1]**2)
        return ans

