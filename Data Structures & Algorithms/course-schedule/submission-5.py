class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aSet = set()
        bSet = set()
        dictionary = dict()

        for a, b in prerequisites:
            if a not in dictionary:
                aNode = Node(a)
                dictionary[a] = aNode
            if b not in dictionary:
                bNode = Node(b)
                dictionary[b] = bNode
            if a == b:
                return False

            aNode, bNode = dictionary[a], dictionary[b]
            aNode.children.append(bNode)

            aSet.add(aNode)
            bSet.add(bNode)

        def findLoop(node):
            stack = [node]
            visited = set()
            while stack:
                cur = stack.pop()
                if cur in visited:
                    return True
                visited.add(cur)
                stack += cur.children
            return False
        
        for node in bSet:
            if findLoop(node):
                return False
        
        return True





        