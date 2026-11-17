class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(0, numCourses, 1):
            adj[i] = []

        for e in prerequisites:
            src, dst = e[0], e[1]
            adj[src].append(dst)

        visit = set()
        def dfs(node, path):
            # print ("I am currently at node: ", node, " with the path set: ", path)
            if node in path:   
                return False #Cycle detected
            if node in visit:
                return True #Fine dfs

            visit.add(node)
            path.add(node)

            for nbr in adj[node]:
                if not dfs(nbr, path):
                    return False
            path.remove(node)
            return True #Fine dfs

        for i in range(0, numCourses):
            if i in visit:
                continue
            if not dfs(i, set()):
                return False

        return True