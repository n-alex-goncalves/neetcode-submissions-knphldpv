class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionary = collections.defaultdict(list)
        for a, b in edges:
            dictionary[a].append(b)
            dictionary[b].append(a)
        
        self.visited = set()
        def dfs(node):
            if node in self.visited:
                return
            self.visited.add(node)
            for neighbour in dictionary[node]:
                dfs(neighbour)
        
        output = 0
        for i in range(n):
            if i not in self.visited:
                output += 1
                dfs(i)
        return output

        