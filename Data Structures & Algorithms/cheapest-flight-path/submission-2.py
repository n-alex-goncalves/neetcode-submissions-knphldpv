class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, cost in flights:
            graph[a].append((b, cost))

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        priorityQueue = [(0, 0, src)] # dist, stops, node

        while priorityQueue:
            d, s, n = heapq.heappop(priorityQueue)

            if s > k:
                continue
            if d > dist[n][s]:
                continue
            
            dist[n][s] = d

            for neighbour, weight in graph[n]:
                distance = weight + d
                stops = s + 1
                if stops <= k + 1 and distance < dist[neighbour][stops]:
                    dist[neighbour][stops] = distance
                    heapq.heappush(priorityQueue, (distance, stops, neighbour))
        
        output = min(dist[dst])
        return output if output != float('inf') else -1