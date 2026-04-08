class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        minimum spanning tree
        pick any point, visited, choose the minimum edge/manhattan distance
        '''
        dist = collections.defaultdict(list)
        for i, (xi, yi) in enumerate(points):
            for j, (xj, yj) in enumerate(points):
                if i == j:
                    continue
                distance = abs(xi - xj) + abs(yi - yj)
                dist[i].append((j, distance))
        
        total = 0

        priorityQueue = [(0, 0)] # weight, index
        visited = set()

        while priorityQueue:
            w, i = heapq.heappop(priorityQueue)

            if i in visited:
                continue
            
            visited.add(i)
            total += w

            for neighbour, weight in dist[i]:
                if neighbour in visited:
                    continue
                heapq.heappush(priorityQueue, (weight, neighbour))
        
        return total


        