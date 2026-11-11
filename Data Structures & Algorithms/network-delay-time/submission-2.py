import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hash_map = self.graphify(times)
        q = []
        if k < 1 or k > n:
            return -1 #k was not found
        best_cost = {}
        heapq.heappush(q, (0, k)) #maps node -> best cost seen so far
        visited = set()
        max_cost = 0
        best_cost[k] = 0
        while q and len(visited) < n:
            curr_details = heapq.heappop(q)
            node, weight = curr_details[1], curr_details[0]
            if node in visited:
                continue
            max_cost = max(max_cost, curr_details[0])
            visited.add(node)
            for nbr in hash_map[node]:
                cost = nbr[1]
                nbr_node = nbr[0]
                if nbr_node in visited:
                    continue
                if nbr_node not in best_cost or weight + cost < best_cost[nbr_node]:
                    best_cost[nbr_node] = weight + cost
                    heapq.heappush(q, (weight + cost, nbr_node))
        if len(visited) < n:
            return -1

        else:
            return max_cost
        
    def graphify(self, times):
        """
        convert the list, times to a dictionary where each key represents the node and key maps to a list of nodes and their weights that the key is connected to.

        example: {1:[(2,1), (4,4)], 2: [(3, 1)], 3: [(4, 1)], 4: []}
        """
        result = defaultdict(list)
        length = len(times)
        for idx in range(0, length, 1):
            current = times[idx]
            source = current[0]
            dst = current[1]
            weight = current[2]
            result[source].append((dst, weight))
        return result




        