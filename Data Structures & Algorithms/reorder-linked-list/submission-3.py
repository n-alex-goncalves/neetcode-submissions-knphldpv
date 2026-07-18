# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            temp1 = cur.next
            cur.next = prev
            prev = cur
            cur = temp1
        return prev

    def splitList(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        return temp

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        cur1 = self.splitList(head)
        cur1 = self.reverseList(cur1)

        while cur1 and head:
            temp1 = head.next
            temp2 = cur1.next
            head.next = cur1
            head.next.next = temp1

            head = temp1
            cur1 = temp2       


        