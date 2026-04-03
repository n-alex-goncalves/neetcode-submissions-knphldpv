# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev

        def printLst(head):
            while head:
                print(head.val)
                head = head.next
            return
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        r = slow.next
        slow.next = None

        r = reverseList(r)
        l = head

        while l and r:
            tempL = l.next
            tempR = r.next

            l.next = r
            r.next = tempL

            l = tempL
            r = tempR
        