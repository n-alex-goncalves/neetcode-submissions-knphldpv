"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        given a root
        use dictionary (?)
        iterate
        '''
        if node == None:
            return None

        dictionary = dict()

        stack = [node]
        visited = set()

        while stack:
            cur = stack.pop(0)

            if cur.val in visited:
                continue

            visited.add(cur.val)
            if cur.val not in dictionary:
                dictionary[cur.val] = Node(cur.val)
    
            stack += cur.neighbors

        stack = [node]
        visited = set()

        while stack:
            cur = stack.pop(0)

            if cur.val in visited:
                continue

            visited.add(cur.val)
            for n in cur.neighbors:
                dictionary[cur.val].neighbors += [dictionary[n.val]]

            stack += cur.neighbors
        
        return dictionary[node.val]
        