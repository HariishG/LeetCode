class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x=abs(sx-fx)
        y=abs(sy-fy)
        distance= max(x,y)
        if distance==0: 
            if t==1:
                return False
            else:
                return True
        return t>=distance
        # if sx==fx and sy==fy and t==1:
        #     return False
        # x=abs(sx-fx)+1
        # y=abs(sy-fy)+1
        # dp=[i for i in range(x)]
        # print(dp)
        # for i in range(1,y):
        #     temp=[None for _ in range(x)]
        #     temp[0]=i
        #     for j in range(1,x):
        #         temp[j]=1+min(temp[j-1], dp[j], dp[j-1])
        #     dp=list(temp)
        # return dp[-1]<=t