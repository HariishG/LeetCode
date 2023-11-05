class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)
        else:
            c=0
            curr=arr[0]
            while c<k:
                if curr>arr[1]:
                    c+=1
                    arr.append(arr.pop(1))
                else:
                    c=1
                    curr=arr[1]
                    arr.append(arr.pop(0))
            return curr