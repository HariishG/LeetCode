prime = [True for i in range(1001)]
prime[0]=prime[1]=False
p=2
while p*p<=1000:
    if prime[p]==True:
        for i in range(p*p,1000,p):
            prime[i]=False
    p+=1
prime[0]=prime[1]=0
prev=2
for i in range(2,1001):
    if prime[i]==True:
        prev=i
    prime[i]=prev

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        nums[0]-=prime[nums[0]-1]
        for i in range(1, len(nums)):
            rem=nums[i]-nums[i-1]-1
            if rem<0:
                return False
            nums[i]-=prime[rem]
        return True