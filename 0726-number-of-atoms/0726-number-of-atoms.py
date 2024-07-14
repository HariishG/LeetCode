class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[defaultdict(int)]
        i=0
        n=len(formula)
        while i<n:
            if formula[i]=='(':
                stack.append(defaultdict(int))
            elif formula[i]==')':
                curr=stack.pop()
                count=""
                while i+1<n and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1

                count=1 if count=="" else int(count)
                prev=stack[-1]
                for e in curr:
                    prev[e]+=curr[e]*count
                
            else:
                element=formula[i]
                count=""
                if i+1<n and formula[i+1].islower():
                    element+=formula[i+1]
                    i+=1
                while i+1<n and formula[i+1].isdigit():
                    count+=formula[i+1]
                    i+=1
                count=1 if count=="" else int(count)
                stack[-1][element]+=count
            i+=1

        cnt=stack[-1]
        ans=""
        for e in sorted(cnt.keys()):
            count="" if cnt[e]==1 else cnt[e]
            ans+=e+str(count)
        return ans

        