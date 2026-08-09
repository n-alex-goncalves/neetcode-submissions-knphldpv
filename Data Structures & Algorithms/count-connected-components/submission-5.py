class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        undirected
        iterate through until len(set) == n
        then return number
        '''

        visited = set()
        dictionary = collections.defaultdict(set)

        for a, b in edges:
            dictionary[a].add(b)
            dictionary[b].add(a)

        def dfs(cur, parent=None):
            if cur in visited:
                return
            
            visited.add(cur)

            for n in dictionary[cur]:
                if n == parent:
                    continue
                dfs(n, cur)
            
            return
        
        output = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            output += 1
            if len(visited) == n:
                return output
        
        return output
        