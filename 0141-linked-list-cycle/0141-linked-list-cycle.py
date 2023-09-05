# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        sp=head
        fp=head
        while fp.next!=None:
            sp=sp.next
            fp=fp.next
            if fp.next:
                fp=fp.next
            else:
                break
            if sp==fp:
                return True
        return False
        
