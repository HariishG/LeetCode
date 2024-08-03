class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        c=Counter(arr)
        for i in target:
            c[i]-=1
        for i in c.values():
            if i!=0:
                return False
        return True

