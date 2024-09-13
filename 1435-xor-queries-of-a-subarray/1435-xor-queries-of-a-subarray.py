class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_lst=[0]
        for i in range(0,len(arr)):
            pre_lst.append(pre_lst[-1]^arr[i])
        ans=[]
        for i in queries:
            ans.append(pre_lst[i[1]+1]^pre_lst[i[0]])
        return ans