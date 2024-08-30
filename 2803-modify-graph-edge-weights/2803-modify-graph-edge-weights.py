class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj=[{}for _ in range(n)]
        for u,v,w in edges:
            adj[u][v]=w
            adj[v][u]=w

        dist=[float('inf') for _ in range(n)]
        dist[source]=0
        def fill():
            nonlocal edges
            for edge in edges:
                if edge[2]==-1:
                    edge[2]=2*10**9
        def dikstras():
            nonlocal dist, pq, adj
            while pq:
                d, node=heapq.heappop(pq)
                for v,w in adj[node].items():
                    if w>0:
                        if dist[v]>dist[node]+w:
                            dist[v]=dist[node]+w
                            heapq.heappush(pq, (dist[v],v))
                            

        pq=[(0, source)]
        dikstras()
        if dist[destination]<target:
            return []
        if dist[destination]==target:
            fill()
            return edges
        for e in edges:
            if e[2]==-1:
                e[2]=1
                adj[e[0]][e[1]]=1
                adj[e[1]][e[0]]=1
                pq=[(dist[e[0]], e[0]), (dist[e[1]], e[1])]
                dikstras()
                if dist[destination]==target:
                    fill()
                    return edges
                if dist[destination]<target:
                    e[2]+=target-dist[destination]
                    adj[e[0]][e[1]]=e[2]
                    adj[e[1]][e[0]]=e[2]
                    fill()
                    return edges
        return []

