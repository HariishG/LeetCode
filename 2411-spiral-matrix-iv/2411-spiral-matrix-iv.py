# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans=[[-1 for _ in range(n)]for _ in range(m)]
        pos=[0,0]
        m-=1
        while head:
            for i in range(n):
                if not head:
                    break
                ans[pos[0]][pos[1]]=head.val
                head=head.next
                pos[1]+=1
            n-=1
            pos[1]-=1
            pos[0]+=1
            for i in range(m):
                if not head:
                    break
                ans[pos[0]][pos[1]]=head.val
                head=head.next
                pos[0]+=1
            m-=1
            pos[0]-=1
            pos[1]-=1
            for i in range(n):
                if not head:
                    break
                ans[pos[0]][pos[1]]=head.val
                head=head.next
                pos[1]-=1
            n-=1
            pos[1]+=1
            pos[0]-=1
            for i in range(m):
                if not head:
                    break
                ans[pos[0]][pos[1]]=head.val
                head=head.next
                pos[0]-=1
            m-=1
            pos[0]+=1
            pos[1]+=1
        return ans

