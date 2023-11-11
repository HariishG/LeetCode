class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.a_list=[[]for _ in range(n)]
        for i in edges:
            self.a_list[i[0]].append([i[1], i[2]])
        

    def addEdge(self, edge: List[int]) -> None:
        self.a_list[edge[0]].append([edge[1], edge[2]])

    def shortestPath(self, node1: int, node2: int) -> int:
        dist=[float('inf') for _ in range(self.n)]
        dist[node1]=0
        pq=[(0, node1)]
        while pq:
            x,y = heapq.heappop(pq)
            if x>dist[y]:
                continue
            if y==node2:
                return x
            for i in self.a_list[y]:
                neigh=i[0]
                cost=i[1]+dist[y]
                if dist[neigh]>cost:
                    dist[neigh]=cost
                    heapq.heappush(pq, (cost, neigh))
        if dist[node2]==float('inf'):
            return -1
        return dist[node2]



# Your a_mat object will be instantiated and called as such:
# obj = a_mat(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)