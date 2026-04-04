class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictionary = collections.defaultdict(list)

        for a, b in prerequisites:
            dictionary[a].append(b)

        self.visited = set()
        def dfs(a):
            if a in self.visited:
                return True # loop
            
            if dictionary[a] == []:
                return False # no loop
            
            self.visited.add(a)
            temp = dictionary[a]
            dictionary[a] = []
    
            for b in temp:
                if dfs(b):
                    return True # loop

            self.visited.remove(a)
            return False # no loop
        
        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True




        