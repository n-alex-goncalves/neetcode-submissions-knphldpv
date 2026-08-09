class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        DFS, ignore parent
        '''
        visited = set()
        dictionary = collections.defaultdict(set)

        for a, b in edges:
            dictionary[a].add(b)
            dictionary[b].add(a)

        def dfs(cur, parent=None):
            if cur in visited:
                return False
            
            visited.add(cur)

            for n in dictionary[cur]:
                if n == parent:
                    continue
                if not dfs(n, cur):
                    return False
            
            return True
        
        if not dfs(0):
            return False

        return len(visited) == n 
