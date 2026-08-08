class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        three-state colouring
        '''
        dictionary = collections.defaultdict(set)
        for a, b in prerequisites:
            dictionary[b].add(a)

        visited = set()
        completed = set()
        
        def dfs(head):
            if head in completed:
                return True

            if head in visited:
                return False
            
            visited.add(head)

            for nxt in dictionary[head]:
                if not dfs(nxt):
                    return False
            
            completed.add(head)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True