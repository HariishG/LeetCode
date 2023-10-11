# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head):
            lst=ListNode()
            ans=lst
            while(head):
                temp1=head.val
                head=head.next
                if(not(head)):
                    lst.val=temp1
                    break
                temp2=head.val
                head=head.next
                if(not(head)):
                    lst.val=temp2
                    lst.next=ListNode()
                    lst=lst.next
                    lst.val=temp1
                    break
                lst.val=temp2
                lst.next=ListNode()
                lst=lst.next
                lst.val=temp1
                lst.next=ListNode()
                lst=lst.next
            return ans
        else:
            return None