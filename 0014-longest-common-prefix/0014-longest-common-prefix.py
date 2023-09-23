class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op=""
        smallest_string=min(strs, key=len)
        for i in range(len(smallest_string)):
            for j in range(len(strs)):
                if smallest_string[i]!=strs[j][i]:
                    return op
            op+=strs[0][i]
        return op