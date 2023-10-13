class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     cost.insert(0, 0)
    #     return self.findCost(cost)

    # def findCost(self, cost):
    #     if cost==[]:
    #         return 0
    #     return min(cost[0]+self.findCost(cost[1:]), cost[0]+self.findCost(cost[2:]))
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=1:
            return 0
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2, len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1], dp[-2])