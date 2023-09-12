class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic=defaultdict(list)
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
        lst=[]
        for i in dic.keys():
            if len(dic[i])>i and i!=0:
                for j in range(0,len(dic[i]),i):
                    lst.append(dic[i][j:j+i])
            else:
                lst.append(dic[i])
        return lst
