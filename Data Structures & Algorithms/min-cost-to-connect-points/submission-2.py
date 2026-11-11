import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.heights = {}
        
        for i in range(1, n + 1, 1):
            self.parent[i] = i
            self.heights[i] = 0
    

    def find(self, n):
        current = n
       
        while (current != self.parent[current]):
            self.parent[current] = self.parent[self.parent[current]]

            current = self.parent[current]
        return current

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False # Cycle detected

        else:
            h1, h2 = self.heights[p1], self.heights[p2]
            if h1 > h2:
                self.parent[p2] = p1
            elif h1 < h2:
                self.parent[p1] = p2

            else:
                self.parent[p2] = p1
                self.heights[p1] += 1
            return True

class Solution:
    def dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        nodes = {}
        for i in range(1, len(points) + 1):
            nodes[i] = points[i - 1]
        q = []
        res = 0
        
        for i in range(1, len(points) + 1):
            p1 = points[i - 1]
            
            for j in range(i + 1, len(points) + 1, 1):
                p2 = points[j - 1]
                distance = self.dist(p1, p2)
                heapq.heappush(q, (distance, i, j))
        
        count = 0
        graph = UnionFind(len(points))
      
        while count < (len(points) - 1):
            
            best_edge = heapq.heappop(q)
            weight, src, dst = best_edge[0], best_edge[1], best_edge[2]
            
            can_union = graph.union(src, dst)
            if not can_union:
                continue
            else:
               
                count += 1
                res = res + weight

        return res



        