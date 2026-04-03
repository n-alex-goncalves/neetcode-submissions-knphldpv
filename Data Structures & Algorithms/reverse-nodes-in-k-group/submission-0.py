# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev


        l, r = head, head
        lst = []
        i = 1
        while r:
            if i == k:
                temp = r.next

                r.next = None
                lst.append(l)
                
                l = temp
                r = temp
                i = 1
                continue

            i += 1
            r = r.next

        lst = [reverseList(x) for x in lst]

        if l:
            lst.append(l)
        
        for i, x in enumerate(lst):
            cur = x
            prev = ListNode(0, x)
            while cur:
                cur = cur.next
                prev = prev.next
            if i + 1 < len(lst):
                prev.next = lst[i + 1]

        return lst[0]

        