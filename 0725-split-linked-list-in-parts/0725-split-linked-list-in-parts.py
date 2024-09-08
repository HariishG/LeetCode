# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        hd=head
        Len=0
        while hd:
            hd=hd.next
            Len+=1
        
        split_size=Len//k
        rem=Len%k
        print(split_size, rem)
        ans=[None for _ in range(k)]
        for i in range(min(Len, k)):
            print(ans)
            if rem>0 and head:
                ans[i]=head
                for j in range(split_size):
                    head=head.next
                temp=head
                head=head.next
                temp.next=None
                rem-=1
            elif head:
                ans[i]=head
                for j in range(split_size-1):
                    head=head.next
                temp=head
                head=head.next
                temp.next=None
        return ans