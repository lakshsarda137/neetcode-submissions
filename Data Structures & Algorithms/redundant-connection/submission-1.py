class UnionFind:
    def __init__(self, n):
        self.height = {}
        self.parent = {}
        for i in range(1, n + 1, 1):
            self.height[i] = 0
            self.parent[i] = i

    def find(self, n):
        """
        goal is to find the ultimate parent of the node, n
        """
        curr = n
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    def union(self, src, dst):
        p1, p2 = self.find(dst), self.find(src)
        if self.find(dst) == self.find(src):
            return False #There is a cycle detected
        else:
            h1, h2 = self.height[p1], self.height[p2]
            if h1 > h2:
                self.parent[p2] = self.find(p1)
            elif h1 < h2:
                self.parent[p1] = self.find(p2)
            else:
                self.parent[p1] = self.find(p2)
                self.height[src] += 1
            return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFind(len(edges))
        for e in edges:
            src, dst = e[0], e[1]
            res = graph.union(src, dst)
            if not res:
                return e
        