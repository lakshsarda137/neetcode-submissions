class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        all_set = set()
        for i in range(0, n, 1):
            all_set.add(i)

        #Now all_set is the set of all nodes

        visited = set()

        for e in edges:
            src, dst = e[0], e[1]
            visited.add(dst)

        diff = all_set - visited
        if len(diff) == 0 or len(diff) >= 2:
            return -1

        final = diff.pop()
        return final