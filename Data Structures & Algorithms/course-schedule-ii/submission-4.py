class Solution:


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for e in prerequisites:
            src, dst = e[0], e[1]
            adj[src].append(dst)
        def dfs(node, path):
            if node in path:
                return False

            if node in visit:
                return True

            visit.add(node)
            path.add(node)
            
            for nbr in adj[node]:
                if not dfs(nbr, path):
                    return False          
            path.remove(node)
            res.append(node)
            return True
        visit = set()
        res = []
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i, set()):
                    return []       
        return res
        