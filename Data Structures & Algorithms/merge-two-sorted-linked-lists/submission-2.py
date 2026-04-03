# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 and list1.val > list2.val:
            list1, list2 = list2, list1

        dummy = ListNode(0, list1)
        prev = ListNode(0, dummy)

        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
                dummy = dummy.next
            else:
                temp = list2.next

                dummy.next = list2
                list2.next = list1

                list2 = temp
                dummy = dummy.next
        
        if list2:
            dummy.next = list2
        
        return prev.next.next
        

        