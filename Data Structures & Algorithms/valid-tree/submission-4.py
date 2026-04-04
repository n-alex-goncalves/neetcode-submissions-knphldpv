class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        all connected
        edges (could go either way, need to track that in dictionary?)
        one pass should visit all (otherwise false)
        '''
        dictionary = collections.defaultdict(list)
        for a, b in edges:
            dictionary[a].append(b)
            dictionary[b].append(a)
            if a == b:
                return False
        
        self.visited = set()

        def dfs(a, parent):
            print(a, parent, self.visited)
            if a in self.visited:
                print("hello")
                return True # loop
            
            self.visited.add(a)
            temp = dictionary[a]
            dictionary[a] = []

            for child in temp:
                if child == parent:
                    continue
                if dfs(child, a):
                    return True # loop
                
            return False

        if dfs(0, None):
            return False

        return len(self.visited) == n
        