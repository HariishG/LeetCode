# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=t=ListNode()
        while head:
            sum=0
            while head and head.val!=0:
                sum+=head.val
                head=head.next
            t.next=ListNode(sum)
            t=t.next
            head=head.next
        return s.next.next