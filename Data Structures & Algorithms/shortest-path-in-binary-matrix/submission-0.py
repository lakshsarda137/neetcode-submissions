import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1, 1), (-1, -1)]

        min_path = float('inf')
        path = 0
        visited = set()
        R, C = len(grid), len(grid[0])
        if (grid[R - 1][C - 1] != 0) or (grid[0][0] != 0):
            return -1
        q = deque()
        q.append((0,0))

        while q:
            length = len(q)
            for _ in range(length):
                coord = q.popleft()
                if coord == (R - 1, C - 1):
                    min_path = min(min_path, path + 1)
                    return min_path

                for dr, dc in directions:
                    x = dr + coord[0]
                    y = dc + coord[1]

                    if x < 0 or y < 0 or x >= R or y >= C or (x,y) in visited or grid[x][y] != 0:
                        continue

                    else:
                        q.append((x, y))
                
                visited.add((coord[0], coord[1]))
            path += 1

        if min_path == float('inf'):
            return -1
        else:
            return min_path
            

            