# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h=head2=head
        while h:
            h=h.next.next
            head2=head2.next
        curr=head2
        curr=curr.next
        head2.next=None
        while curr:
            temp=curr
            curr=curr.next
            temp.next=head2
            head2=temp
        ans=0
        while head2:
            ans=max(ans, head.val+head2.val)
            head=head.next
            head2=head2.next
        return ans