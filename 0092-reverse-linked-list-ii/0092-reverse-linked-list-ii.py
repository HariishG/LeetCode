# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        head=ListNode(0, head)
        curr=head
        for i in range(left-1):
            curr=curr.next
        rev_pos=curr
        rev_tail=curr.next
        for i in range(right-left+2):
            temp=curr
            curr=curr.next
            temp.next=rev_pos.next
            rev_pos.next=temp
        rev_tail.next=curr
        return head.next