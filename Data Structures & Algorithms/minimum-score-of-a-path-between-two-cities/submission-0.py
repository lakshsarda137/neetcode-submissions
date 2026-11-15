class Solution:
    def graphify(self, n, roads):
        graph = {}
        for node in range(1, n + 1, 1):
            graph[node] = []
        for e in roads:
            n1, n2, w = e[0], e[1], e[2]
            graph[n1].append((n2, w))
            graph[n2].append((n1, w))
            
        return graph


    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = self.graphify(n, roads)
        stack = [1, n]
        visited = set()
        # visited.add(1)
        # visited.add(n)
        result = float('inf')
        while len(stack) > 0:
            current = stack.pop(-1)
            if current in visited:
                continue
            else:
                visited.add(current)
            for nbr in graph[current]:
                node, weight = nbr[0], nbr[1]
                result = min(weight, result)
                if node not in visited:
                    stack.append(node)
            

        return result