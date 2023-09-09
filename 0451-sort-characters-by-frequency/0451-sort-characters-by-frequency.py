class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        sorted_list=sorted(dic.items(), key = lambda x:x[1], reverse = True)
        new_s=''
        for i in sorted_list:
            new_s+=i[0]*i[1]
        return new_s
