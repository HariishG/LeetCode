class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=Counter(arr)
        st=set()
        for i in d:
            if d[i]==1:
                st.add(i)
        for i in arr:
            if i in st:
                k-=1
            if k==0:
                return i
        return ""

