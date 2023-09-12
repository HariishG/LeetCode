class Solution:
    def minDeletions(self, s: str) -> int:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lst_tup = list(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
        lst = [list(i) for i in lst_tup]
        count=0
        for i in range(len(lst)-1):
            for j in range(i+1,len(lst)):
                if lst[i][1] == lst[j][1] != 0:
                    count+=1
                    lst[j][1]-=1
        return count