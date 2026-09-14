class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        R, C = len(isConnected), len(isConnected[0])
        graph = {}
        for r in range(R):
            for c in range(C):
                if isConnected[r][c] == 1:
                    if r in graph:
                        graph[r].append(c)
                    else:
                        graph[r] = [c]
        all_nodes = set()
        for num in range(R):
            all_nodes.add(num)
        def dfs(node, visit):
            if node in visit:
                return visit
            visit.add(node)
            for nbr in graph[node]:
                dfs(nbr, visit)
            return visit
        found = set()
        iterations = 0
        for curr_node in range(R):
            if curr_node in found:
                continue
            else:
                iterations += 1
                add = dfs(curr_node, set())
                found = found.union(add)
        return iterations



            
