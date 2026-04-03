# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        while cur:
            temp = 2
            1 -> prev -> 2
                        &



        prev -> 1 -> 2 -> 3
        '''
        prev = None
        while head:
            temp = head.next
            head.next = prev

            prev = head
            head = temp
        return prev
        