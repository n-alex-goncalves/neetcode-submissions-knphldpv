# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(lists)

        head = ListNode(0)
        dummy = ListNode(0, head)

        while lists:
            val, i, cur = heapq.heappop(lists)
            head.next = cur
            head = head.next

            cur = cur.next
            if cur:
                heapq.heappush(lists, (cur.val, i, cur))
        
        return dummy.next.next
