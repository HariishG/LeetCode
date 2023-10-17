# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        curr=curr.next
        head.next=None
        while curr.next!=None:
            temp=curr
            curr=curr.next
            temp.next=head
            head=temp
        curr.next=head
        head=curr
        return head