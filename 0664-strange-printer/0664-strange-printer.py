class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(char for char, _ in itertools.groupby(s))
        dp = {}
        def func(start, end):
            if start > end:
                return 0
            if (start, end) in dp:
                return dp[(start, end)]
            Min = 1+func(start+1, end)
            for k in range(start+1, end+1):
                if s[k] == s[start]:
                    temp = func(start, k-1) + func(k+1, end)
                    Min = min(Min, temp)
            dp[(start, end)] = Min
            return Min
        return func(0, len(s) - 1)