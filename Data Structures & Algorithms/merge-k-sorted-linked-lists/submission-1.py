# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(lst)

        tail = dummy = ListNode(0)
        while lst:
            val, index, node = heapq.heappop(lst)
            dummy.next = node
            
            dummy = dummy.next
            node = node.next

            if node:
                heapq.heappush(lst, (node.val, index, node))

        return tail.next
        