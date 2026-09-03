class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])

            elif edge[0] not in graph:
                graph[edge[0]] = [edge[1]]

            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            
            elif edge[1] not in graph:
                graph[edge[1]] = [edge[0]]


        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            if node in graph:
                for nbr in graph[node]:
                    dfs(nbr)

            return
        res = 0
        while len(visited) < n:
            for node in range(n):
                
                if node not in visited:
                    res += 1
                    dfs(node)

        return res
