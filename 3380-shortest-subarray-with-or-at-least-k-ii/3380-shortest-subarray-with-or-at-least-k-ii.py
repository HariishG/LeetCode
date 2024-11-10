class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        set_bits=[0 for _ in range(32)]
        res=float('inf')
        i=0
        j=0
        curr=0
        while i<n:
            curr|=nums[i]
            for pos in range(32):
                if nums[i]>>pos&1:
                    set_bits[pos]+=1
                
            while j<=i and curr>=k:
                res=min(res,i-j+1)
                for pos in range(32):
                    if nums[j]>>pos&1:
                        set_bits[pos]-=1
                    if set_bits[pos]==0:
                        curr&=~(1<<pos)
                j+=1
            i+=1
        if res==float('inf'):
            return -1    
        return res

