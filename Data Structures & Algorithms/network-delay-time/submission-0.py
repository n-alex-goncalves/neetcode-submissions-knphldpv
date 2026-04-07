class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        perform dijkstra
        return sum
        if inf, return -1
        '''
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t)) # source, target, time 

        dist = {x: float('inf') for x in range(1, n + 1)}
        dist[k] = 0

        priorityQueue = [(0, k)] # weight, node

        while priorityQueue:
            w, n = heapq.heappop(priorityQueue)

            if w > dist[n]:
                continue
            dist[n] = w

            for target, time in graph[n]:
                distance = w + time

                if distance < dist[target]:
                    dist[target] = distance
                    heapq.heappush(priorityQueue, (distance, target))
        
        total = max(dist.values())
        return total if total != float('inf') else -1