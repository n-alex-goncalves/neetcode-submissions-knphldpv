class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dictionary = collections.defaultdict(list)
        for a, b in prerequisites:
            dictionary[a].append(b)
        
        self.visited = set()

        def dfs(a):
            if a in self.visited:
                return False
            
            self.visited.add(a)
            for b in dictionary[a]:
                if not dfs(b):
                    return False
            self.visited.remove(a)

            dictionary[a] = []

            return True

        for i in range(numCourses):
            print(self.visited)
            if not dfs(i):
                return False
        
        return True
