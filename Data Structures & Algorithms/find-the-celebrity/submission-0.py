# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        loser_set = set() #Node: People who know someone
        all_nodes = set()
        famous = set()
        for node in range (n):
            all_nodes.add(node)
            node_known = 0
            for neighbor in range(n):
                if node != neighbor:
                    if knows(neighbor, node):
                        node_known += 1
                        loser_set.add(neighbor)
            if node_known == (n-1):
                famous.add(node)
        clueless = all_nodes - loser_set
        for node in range (n):
            if node in famous and clueless:
                return node
        return -1


        
                        