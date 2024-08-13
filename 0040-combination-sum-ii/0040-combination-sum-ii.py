class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def func(i,s):
            if s>target:
                return
            if i>=len(candidates):
                if s==target:
                    self.ans.append(list(self.arr))
                return

            self.arr.append(candidates[i])
            s+=candidates[i]
            func(i+1, s)
            s-=candidates[i]
            self.arr.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            func(i+1, s)

        self.arr=[]
        self.ans=[]
        func(0, 0)
        return self.ans
                    