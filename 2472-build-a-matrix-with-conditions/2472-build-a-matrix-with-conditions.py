class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)

            for neigh in adj[src]:
                if not dfs(neigh, adj, visit, path, order):
                    return False

            path.remove(src)
            order.append(src)
            return True

        def topo_sort(edges):
            adj=defaultdict(list)
            for i,j in edges:
                adj[i].append(j)
            visit=set()
            path=set()
            order=[]
            for src in range(1,k+1):
                if not dfs(src, adj, visit, path, order):
                    return []
            return order[::-1]

        row_order=topo_sort(rowConditions)
        col_order=topo_sort(colConditions)
        if not row_order or not col_order:
            return []

        row_val={n:i for i,n in enumerate(row_order)}
        col_val={n:i for i,n in enumerate(col_order)}

        ans=[[0]*k for _ in range(k)]
        for i in range(1,k+1):
            r,c=row_val[i], col_val[i]
            ans[r][c]=i
        return ans