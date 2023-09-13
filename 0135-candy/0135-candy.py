class Solution:
    def candy(self, ratings: List[int]) -> int:
        c=[1 for _ in range(len(ratings))]
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                c[i]=c[i-1]+1
        for i in range(-2,-1*len(ratings)-1,-1):
            if ratings[i]>ratings[i+1] and c[i]<c[i+1]+1:
                c[i]=c[i+1]+1
        return sum(c)