class Solution:
    def secondHighest(self, s: str) -> int:
        d=defaultdict(int)
        for i in s:
            if i.isdigit():
                d[i]+=1
        lst=[]
        for i in d.keys():
            lst.append(int(i))
        lst.sort(reverse=True)
        if len(lst)>1:
            return lst[1]
        return -1