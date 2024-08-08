class Solution:
    def originalDigits(self, s: str) -> str:
        d=defaultdict(int)
        c=Counter(s)
        d[0]=c['z']
        c['e']-=c['z']
        c['r']-=c['z']
        c['o']-=c['z']
        c['z']=0

        d[2]=c['w']
        c['t']-=c['w']
        c['o']-=c['w']
        c['w']=0

        d[4]=c['u']
        c['f']-=c['u']
        c['o']-=c['u']
        c['r']-=c['u']
        c['u']=0

        d[6]=c['x']
        c['s']-=c['x']
        c['i']-=c['x']
        c['x']=0

        d[8]=c['g']
        c['e']-=c['g']
        c['i']-=c['g']
        c['h']-=c['g']
        c['t']-=c['g']
        c['g']=0

        d[1]=c['o']
        c['n']-=c['o']
        c['e']-=c['o']
        c['o']=0

        d[3]=c['h']
        c['t']-=c['h']
        c['r']-=c['h']
        c['e']-=2*c['h']
        c['h']=0
        
        d[5]=c['f']
        c['i']-=c['f']
        c['v']-=c['f']
        c['e']-=c['f']
        c['f']=0

        d[7]=c['s']
        c['e']-=2*c['s']
        c['v']-=c['s']
        c['n']-=c['s']
        c['s']=0

        d[9]=c['n']//2
        ans=""
        for i in range(10):
            ans+=str(i)*d[i]
        return ans