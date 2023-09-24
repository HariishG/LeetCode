class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if digits=="":
            return []
        op=[]
        def find(rem_dig, curr_seq=""):
            if len(rem_dig)==1:
                for i in letters[int(rem_dig)-2]:
                    op.append(curr_seq+i)
            else:
                for i in letters[int(rem_dig[0])-2]:
                    find(rem_dig[1:], curr_seq+i)
        find(digits)
        return op