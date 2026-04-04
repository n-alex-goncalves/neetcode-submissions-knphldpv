class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionary = collections.defaultdict(list)
        nodes = set([range(n)])
        for a, b in edges:
            dictionary[a].append(b)
            dictionary[b].append(a)

        self.visited = set()
        def dfs(a, parent):
            if a in self.visited:
                return True
            
            self.visited.add(a)
            temp = dictionary[a]
            dictionary[a] = []

            for child in temp:
                if child == parent:
                    continue
                dfs(child, a)
        
        output = 0
        for i in range(n):
            if nodes == self.visited:
                return output
            if i in self.visited:
                continue
            dfs(i, None)
            output += 1
        return output
        