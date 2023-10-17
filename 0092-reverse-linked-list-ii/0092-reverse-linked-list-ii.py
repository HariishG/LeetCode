# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        head=ListNode(next=head)
        curr=head
        l=1
        while  curr.next!=None and l<left:
            curr=curr.next
            l+=1
        rev_pos=curr
        rev_tail=curr.next
        while curr.next!=None and l<=right:
            temp=curr
            curr=curr.next
            temp.next=rev_pos.next
            rev_pos.next=temp
            l+=1
        rev_tail.next=curr.next
        curr.next=rev_pos.next
        rev_pos.next=curr
        return head.next