class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        for i in range(len(edges)):
            u,v=edges[i]
            adj[u].append([v,succProb[i]])
            adj[v].append([u,succProb[i]])

        pq=[(-1, start_node)]
        visit=set()
        while pq:
            prob, node = heapq.heappop(pq)
            visit.add(node)
            if node==end_node:
                return prob*-1
            for nei, nei_prob in adj[node]:
                if nei not in visit:
                    heapq.heappush(pq, (nei_prob*prob, nei))
        return 0

