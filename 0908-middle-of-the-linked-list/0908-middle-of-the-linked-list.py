# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        t=head
        n=1
        while t.next:
            t=t.next
            n+=1
        n=n//2
        while n>0:
            head=head.next
            n-=1
        return head
