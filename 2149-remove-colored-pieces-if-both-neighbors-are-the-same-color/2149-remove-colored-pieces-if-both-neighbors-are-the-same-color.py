class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a=0
        b=0
        for i in range(1,len(colors)-1):
            if colors[i-1]==colors[i+1]==colors[i]=='A':
                a+=1
            elif colors[i-1]==colors[i+1]==colors[i]=='B':
                b+=1
        if a>b:
            return True
        return False