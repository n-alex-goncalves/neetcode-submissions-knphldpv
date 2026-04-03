"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tail = dummy = Node(0, None)
        dictionary = {None: None}

        cur = head
        while cur:
            dictionary[cur] = Node(cur.val, 0)
            cur = cur.next
        
        cur = head
        dummy.next = dictionary[cur]
        dummy = dummy.next
        while cur:
            dummy.next = dictionary[cur.next]
            dummy.random = dictionary[cur.random]

            dummy = dummy.next
            cur = cur.next

        
        return tail.next