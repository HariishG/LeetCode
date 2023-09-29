# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head
        while t.next:
            t.next=ListNode(gcd(t.val, t.next.val), t.next)
            t=t.next.next
        return head