class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        s=0
        for i in range(1, n+1):
            if target[s]==i:
                ans.append("Push")
                s+=1
            else:
                ans.append("Push")
                ans.append("Pop") 
            if s==len(target):
                break
        # for i in range(n-target[-1]):
        #     ans.append("Push")
        #     ans.append("Pop")
        return ans