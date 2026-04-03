# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp
            return prev
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        r = slow.next
        slow.next = None
        
        r = reverseList(r)
        l = head

        while l and r:
            temp1 = l.next
            temp2 = r.next

            l.next = r
            l.next.next = temp1

            l = temp1
            r = temp2
        
        