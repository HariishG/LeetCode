# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=head
        t=head.next
        sum=0
        while t:
            if t.val==0:
                s=s.next
                s.val=sum
                sum=0
            else:
                sum+=t.val
            t=t.next
        s.next=None
        return head.next