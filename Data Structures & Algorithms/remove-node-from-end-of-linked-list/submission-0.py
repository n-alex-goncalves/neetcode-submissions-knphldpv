# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, slow, fast = ListNode(0, head), ListNode(0, head), head

        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return dummy.next.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next.next
        slow.next = temp

        return dummy.next 
        
        
        