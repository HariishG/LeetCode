class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        k=k%s
        print(k)
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
            k-=chalk[i]