class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst=[]
        for i in arr:
            lst.append([i,bin(i).count('1')])
        lst.sort(key=lambda a: [a[1],a[0]])
        for i in range(len(lst)):
            lst[i]=lst[i][0]
        return lst