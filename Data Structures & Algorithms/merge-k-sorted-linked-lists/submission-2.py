# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(x.val, i, x) for i, x in enumerate(lists)]
        heapq.heapify(heap)

        cur = ListNode()
        dummy = ListNode(next=cur)
        while heap:
            val, index, lst = heapq.heappop(heap)
            cur.next = lst
            cur = cur.next

            if lst.next:
                heapq.heappush(heap, (lst.next.val, index, lst.next))
        
        return dummy.next.next