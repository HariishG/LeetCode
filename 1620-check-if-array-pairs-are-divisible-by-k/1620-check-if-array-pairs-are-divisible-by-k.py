class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count=0
        zero_count=0
        d=defaultdict(int)
        for num in arr:
            rem=(num%k+k)%k
            if rem==0:
                zero_count^=1
            else:
                if d[k-rem]>0:
                    count-=1
                    d[k-rem]-=1
                else:
                    count+=1
                    d[rem]+=1
        return count==0 and zero_count==0
