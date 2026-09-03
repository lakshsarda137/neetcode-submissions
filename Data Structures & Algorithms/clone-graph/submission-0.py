"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = {} #Maps node value: value of neighbors
        hash_objects = {} #Maps node values to corresponding objects

        def dfs(current):
            if current is None:
                return
            if current.val in hash_objects:
                return
            
            hash_objects[current.val] = Node(current.val, [])
            
            for nbr in current.neighbors:
                if current.val in hash_map:
                    hash_map[current.val].append(nbr.val)
                else:
                    hash_map[current.val] = [nbr.val]

                dfs(nbr)
            return
        dfs(node)
        for current_node_val in hash_map:
            for nbrs_val in hash_map[current_node_val]:
                nbr_object = hash_objects[nbrs_val]
                origin_object = hash_objects[current_node_val]
                origin_object.neighbors.append(nbr_object)

        return hash_objects[node.val]
