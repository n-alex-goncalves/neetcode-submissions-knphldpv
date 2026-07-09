# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            temp1 = cur.next
            temp2 = cur
        
            cur.next = prev

            cur = temp1
            prev = temp2
        
        return prev